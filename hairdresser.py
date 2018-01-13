import copy
from datetime import datetime, date, timedelta
from intervaltree import IntervalTree

class ScheduleItem(object):
    def __init__(self, appointment_type, start_time, end_time):
        self.appointment_type= appointment_type
        self.start_time = start_time
        self.end_time = end_time
    def get_begin(self):
        return minutes_from_midnight(self.start_time)
    def get_end(self):
        return minutes_from_midnight(self.end_time)

def minutes_from_midnight(time):
    str_time = datetime.strptime(time, '%I:%M%p').time()
    midnight = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    return int((datetime.combine(date.today(), str_time) - midnight).total_seconds()/60)

class HairDresserScheduler(object):
    def __init__(self):
        self.Schedule = []

        while True:
            self.display_instructions()
            entered = raw_input(">> Please type a command: ")
            if entered == 'exit':
                print 'See you later.'
                break
            elif entered:
                self.process_command(entered)
            else:
                self.display_instructions()
                raw_input(">> Please type a command: ")

    def display_instructions(self):
        print '\n Commands Available: \n'
        print ' list - will list all future appointments'
        print ' schedule - will enable an appointment to be booked'
        print ' exit - stop the program \n'

    def process_command(self, command):
        if command == 'list':
            self.print_table()
        elif command == 'schedule':
            self.init_schedule_item()
        else:
            return

    def init_schedule_item(self):
        print "\n What kind of appointment?"
        print "\n a) Haircut (30 mins) \n b) Shampoo & Haircut (1 hr) \n"
        schedule_option = raw_input(">> Select an option (i.e. a): ")

        if (schedule_option == 'a') or (schedule_option == 'a)'):
            self.schedule_appointment('haircut')
        elif (schedule_option == 'b') or (schedule_option == 'b)'):
            self.schedule_appointment('shampoo_haircut')
        else:
            print 'Incorrect input. Please try again.'
            return

    def get_appointment_end(self, appointment_start, schedule_type):
        midnight = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        mytime = datetime.strptime(appointment_start, "%I:%M%p").time()
        mydatetime = (datetime.combine(date.today(), mytime))

        if schedule_type == "haircut":
            new_mydatetime = mydatetime + timedelta(minutes=30)
        else:
            new_mydatetime = mydatetime + timedelta(minutes=60)

        if new_mydatetime < datetime.now():
            return False

        if midnight.date() < new_mydatetime.date():
            return False

        return new_mydatetime.strftime("%I:%M%p")

    def schedule_appointment(self, schedule_type):
        print "\n When would you like to schedule the appointment? \n"
        appointment_time = raw_input('>> Please enter a time (i.e. 9:00AM): ')
        if appointment_time:
            try:
                appointment_end = self.get_appointment_end(appointment_time, schedule_type)

                # break if the appointment ends after midnight
                if appointment_end == False:
                    print '\n Invalid appointment time.'
                    return

                if len(self.Schedule) == 0:
                    self.Schedule.append(ScheduleItem(schedule_type, appointment_time, appointment_end))
                    self.ScheduleTree = IntervalTree(self.Schedule)
                    print '\n Success, an appointment has been booked.'
                    self.print_table()
                else:
                    free_time_slot = len(self.ScheduleTree.search(minutes_from_midnight(appointment_time), minutes_from_midnight(appointment_end))) == 0

                    if free_time_slot:
                        self.Schedule.append(ScheduleItem(schedule_type, appointment_time, appointment_end))
                        self.ScheduleTree = IntervalTree(self.Schedule)
                        print '\n Success, an appointment has been booked.'
                        self.print_table()
                    else:
                        print '\n Sorry, that time has been booked.'
                        return
            except ValueError:
                print '\n Unable to process your request. Please try again.'
                return
        else:
            print '\n No time entered. Please try again.'
            return

    def get_schedule_values(self, arr):
        return [(item.appointment_type, item.start_time, item.end_time) for item in arr]

    def print_table(self, separate_head=True):
        # Get all future appointments
        now = datetime.now().strftime('%I:%M%p')
        schedule = []
        if len(self.Schedule) > 0:
          schedule_array = copy.deepcopy(self.ScheduleTree.search(minutes_from_midnight(now), minutes_from_midnight("11:59PM")))
          schedule = self.get_schedule_values(schedule_array)
        schedule.insert(0, ("Name", "Start", "End"))

        # Count the column width
        widths = []
        for line in schedule:
          for i,size in enumerate([len(x) for x in line]):
              while i >= len(widths):
                  widths.append(0)
              if size > widths[i]:
                  widths[i] = size

        # Generate the format string to pad the columns
        print_string = ""
        for i,width in enumerate(widths):
          print_string += "{" + str(i) + ":" + str(width) + "} | "
        if (len(print_string) == 0):
          return
        print_string = print_string[:-3]

        # Print the actual data
        print
        for i,line in enumerate(schedule):
          print(' ' + print_string.format(*line))
          if (i == 0 and separate_head):
              print(' ' + "-"*(sum(widths)+3*(len(widths)-1)))
        print

if __name__ == "__main__":
    HairDresserScheduler()
