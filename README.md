Timetable Generator for Multiple Sections  
=========================================  

Description  
-----------  
This Python project generates a timetable for multiple sections with:  
- Randomly assigned subjects, professors, and rooms  
- No consecutive repetitions of professors or rooms in the same section  
- Clean and structured output displayed in table format using `tabulate`  
- Timetable is saved as a CSV file for easy reference  

Features  
--------  
- Generates a weekly timetable for multiple sections (e.g., MCA Section A and Section B)  
- Randomly assigns:  
  - Subjects (e.g., DSA, DBMS, OS, CN, ML)  
  - Professors (e.g., Prof. Sharma, Prof. Verma)  
  - Rooms (e.g., Room 101, Room 102)  
- Ensures:  
  - No consecutive repetition of professors or rooms  
  - Proper scheduling across multiple sections  
- Displays the timetable in a formatted table in the terminal using `tabulate`  
- Saves the timetable as a CSV file  

Technologies Used  
-----------------  
- Python  
- pandas: For creating and exporting the timetable to a CSV file  
- tabulate: For displaying the timetable in a readable table format  

Installation and Usage  
----------------------  
Install dependencies:  
```
pip install pandas tabulate  
```


Customization  
-------------  
I can easily modify the project by:  
- Changing the sections, subjects, professors, and rooms  
- Adding more time slots or days  
- Tweaking the randomization logic to suit your needs  

Future Improvements  
-------------------  
- Add support for custom time slots and days  
- Implement a GUI interface for better user interaction  
- Add teacher constraints to avoid assigning the same professor across sections at the same time
