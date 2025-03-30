import pandas as pd
import random
import os
from tabulate import tabulate

# Define the MCA sections, professors, rooms, and time slots
sections = ["MCA Section A", "MCA Section B"]
professors = ["Prof. Sharma", "Prof. Verma", "Prof. Singh", "Prof. Gupta", "Prof. Reddy"]
rooms = ["Room 101", "Room 102", "Room 103", "Room 104"]
subjects = ["DSA", "DBMS", "OS", "CN", "ML"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
time_slots = ["9:00-10:00", "10:00-11:00", "11:15-12:15", "12:15-1:15", "2:00-3:00"]

# Generate timetable
timetable = []

# Logic: Each section has a different schedule
for section in sections:
    for day in days:
        used_professors = set()  # To avoid same professor in consecutive slots
        used_rooms = set()       # Avoid same room back-to-back
        for slot in time_slots:
            # Ensure random selection with no immediate repeats
            available_professors = list(set(professors) - used_professors)
            available_rooms = list(set(rooms) - used_rooms)

            # Assign random professor and room
            professor = random.choice(available_professors)
            room = random.choice(available_rooms)
            subject = random.choice(subjects)

            # Append to timetable
            timetable.append([section, day, slot, subject, professor, room])

            # Track used professors and rooms
            used_professors.add(professor)
            used_rooms.add(room)

# Convert to DataFrame
df = pd.DataFrame(timetable, columns=["Section", "Day", "Time", "Subject", "Professor", "Room"])

# Save CSV to the current directory
output_file = os.path.join(os.getcwd(), 'timetable_mca.csv')
df.to_csv(output_file, index=False)

# Display the timetable in a readable table format
print("\nTimetable for MCA Sections:\n")
print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

print(f"\n✅ Timetable saved to {output_file}")
