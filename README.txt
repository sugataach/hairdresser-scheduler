# Author: Sugata Acharjya
# Date: Nov 22, 2016

# HairDresserScheduler

- README.txt: This file. Overview of the project.
- hairdresser.py: Scheduler program. Contains classes relevant to running the program.
- intervaltree.py: Record-keeping data structure. Contains Interval Tree implementation.

## How to Run

1. Install Python (https://www.python.org/downloads/)
2. Open a terminal/command-line.
3. Navigate to `HairDresserScheduler` folder.
4. Type and run `python hairdresser.py`
5. Enjoy.

## Implementation Details

1. Appointments can only be booked on the current calendar day (no appointments can end on midnight or later of the current day).
2. Appointments cannot be booked for times prior to the current system time.
3. The `list` command will only show upcoming appointments, based on current system time.
4. The `schedule` command is split into 2 parts (Part 1: Type of Appointment, Part 2: Time of Appointment) for UX consideration.
5. The user input for `schedule` is strictly defined and will not process malformed input.

## Design Considerations

The data structure chosen for record keeping is an interval tree (https://en.wikipedia.org/wiki/Interval_tree). Interval trees have a query time of O(log n + m) and an initial creation time of O(n log n), while limiting memory consumption to O(n). They can efficiently find all intervals that overlap with any given interval or point.

It was very useful for the windowing queries performed to check for scheduling conflicts and dynamically printing appointments. The interval tree used in this project is an augmented Binary Search Tree.

Python was chosen as the implementation language given it's expressiveness and rich standard library. Of particular note is the Python datetime library which was critical for querying functionality.

## Logs


Example: Create a `haircut` appointment at 9:00AM and a `shampoo_haircut` appointment at 2:00PM and exit.


```
» python hairdresser.py

 Commands Available:

 list - will list all future appointments
 schedule - will enable an appointment to be booked
 exit - stop the program

>> Please type a command: schedule

 What kind of appointment?

 a) Haircut (30 mins)
 b) Shampoo & Haircut (1 hr)

>> Select an option (i.e. a): a

 When would you like to schedule the appointment?

>> Please enter a time (i.e. 9:00AM): 9:00AM

 Success, an appointment has been booked.

 Name    | Start  | End
 --------------------------
 haircut | 9:00AM | 09:30AM


 Commands Available:

 list - will list all future appointments
 schedule - will enable an appointment to be booked
 exit - stop the program

>> Please type a command: schedule

 What kind of appointment?

 a) Haircut (30 mins)
 b) Shampoo & Haircut (1 hr)

>> Select an option (i.e. a): b

 When would you like to schedule the appointment?

>> Please enter a time (i.e. 9:00AM): 9:30AM

 Sorry, that time has been booked.

 Commands Available:

 list - will list all future appointments
 schedule - will enable an appointment to be booked
 exit - stop the program

>> Please type a command: exit
See you later.
sugata at Air in ~/Playground
»
sugata at Air in ~/Playground
» python hairdresser.py

 Commands Available:

 list - will list all future appointments
 schedule - will enable an appointment to be booked
 exit - stop the program

>> Please type a command: schedule

 What kind of appointment?

 a) Haircut (30 mins)
 b) Shampoo & Haircut (1 hr)

>> Select an option (i.e. a): a

 When would you like to schedule the appointment?

>> Please enter a time (i.e. 9:00AM): 9:00AM

 Success, an appointment has been booked.

 Name    | Start  | End
 --------------------------
 haircut | 9:00AM | 09:30AM


 Commands Available:

 list - will list all future appointments
 schedule - will enable an appointment to be booked
 exit - stop the program

>> Please type a command: schedule

 What kind of appointment?

 a) Haircut (30 mins)
 b) Shampoo & Haircut (1 hr)

>> Select an option (i.e. a): b

 When would you like to schedule the appointment?

>> Please enter a time (i.e. 9:00AM): 2:00PM

 Success, an appointment has been booked.

 Name            | Start  | End
 ----------------------------------
 haircut         | 9:00AM | 09:30AM
 shampoo_haircut | 2:00PM | 03:00PM


 Commands Available:

 list - will list all future appointments
 schedule - will enable an appointment to be booked
 exit - stop the program

>> Please type a command: exit
See you later.
```

Example: Create a `haircut` appointment at 9:00AM and try to book a conflicting `shampoo_haircut` appointment at 9:30AM.


```
» python hairdresser.py

 Commands Available:

 list - will list all future appointments
 schedule - will enable an appointment to be booked
 exit - stop the program

>> Please type a command: schedule

 What kind of appointment?

 a) Haircut (30 mins)
 b) Shampoo & Haircut (1 hr)

>> Select an option (i.e. a): a

 When would you like to schedule the appointment?

>> Please enter a time (i.e. 9:00AM): 9:00AM

 Success, an appointment has been booked.

 Name    | Start  | End
 --------------------------
 haircut | 9:00AM | 09:30AM


 Commands Available:

 list - will list all future appointments
 schedule - will enable an appointment to be booked
 exit - stop the program

>> Please type a command: schedule

 What kind of appointment?

 a) Haircut (30 mins)
 b) Shampoo & Haircut (1 hr)

>> Select an option (i.e. a): b

 When would you like to schedule the appointment?

>> Please enter a time (i.e. 9:00AM): 9:30AM

 Sorry, that time has been booked.

 Commands Available:

 list - will list all future appointments
 schedule - will enable an appointment to be booked
 exit - stop the program

>> Please type a command: exit
See you later.
```


Example: Try to create a `shampoo_haircut` appointment at 11:00PM (which ends at 12:00AM, next day).


```
» python hairdresser.py

 Commands Available:

 list - will list all future appointments
 schedule - will enable an appointment to be booked
 exit - stop the program

>> Please type a command: schedule

 What kind of appointment?

 a) Haircut (30 mins)
 b) Shampoo & Haircut (1 hr)

>> Select an option (i.e. a): b

 When would you like to schedule the appointment?

>> Please enter a time (i.e. 9:00AM): 11:30PM

 Invalid appointment time.

 Commands Available:

 list - will list all future appointments
 schedule - will enable an appointment to be booked
 exit - stop the program

>> Please type a command: exit
See you later.
```
