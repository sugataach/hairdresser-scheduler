from datetime import datetime, date
from intervaltree import IntervalTree

class ScheduleItem:
    def __init__(self, course_number, start_time, end_time):
        self.course_number = course_number
        self.start_time = start_time
        self.end_time = end_time
    def get_begin(self):
        return minutes_from_midnight(self.start_time)
    def get_end(self):
        return minutes_from_midnight(self.end_time)
    def __repr__(self):
        return ''.join(["{ScheduleItem: ", str((self.course_number, self.start_time, self.end_time)), "}"])

def minutes_from_midnight(time):
    str_time = datetime.strptime(time, '%I:%M%p').time()
    midnight = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    return int((datetime.combine(date.today(), str_time) - midnight).total_seconds()/60)

T = IntervalTree([ScheduleItem(28374, "9:00AM", "10:00AM"), \
                  ScheduleItem(43564, "8:00AM", "12:00PM"), \
                  ScheduleItem(53453, "1:00AM", "2:00AM")])
print T.search(minutes_from_midnight("9:00PM"), minutes_from_midnight("10:00PM"))
