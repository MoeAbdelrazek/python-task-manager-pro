#  Python Task Manager Pro

##  Overview
Command-line Task Manager Pro built in Python as part of the Programming in Python by Meta (Coursera) course.  
Uses JSON for structured task storage and demonstrates Python fundamentals in a professional project format.

---

##  Features
-  Add tasks (title & description)  
-  View all tasks with completion status  
-  Mark tasks as completed  
-  Delete tasks  
-  Save tasks to a JSON file (tasks.json)  
-  Load tasks from a JSON file (tasks.json)  

---

##  Skills Demonstrated
- Variables & data types  
- Lists & dictionaries  
- Functions & modular code  
- Loops(for, while) & conditionals (if/else)  
- File handling with JSON (json module)  
- Exception handling (try/except)
- Terminal input/output  

---

##  Project Structure
python-task-manager-pro/  
├── task_manager.py   # Main program  
├── tasks.json        # Saved tasks  
└── README.md         # Documentation  

---

---

 Usage  
When you run the program, you’ll see:  

--- Task Manager ---  
1. Add a task  
2. View all tasks  
3. Mark task as completed  
4. Delete a task  
5. Save tasks to file  
6. Load tasks from file  
7. Exit  
Enter your choice (1-7):  

---

### Examples

**Add a task**  
Enter your choice (1-7): 1  
Enter task title: Study Python  
Enter task description: Finish Meta course assignment  
Task 'Study Python' added successfully!  

**View tasks**  
1. Study Python - Finish Meta course assignment [❌ Not Completed]  

**JSON Storage Example**  
[
  {
    "title": "Study Python",
    "description": "Finish Meta course assignment",
    "completed": false
  },
  {
    "title": "Exercise",
    "description": "Run 5km",
    "completed": true
  }
]  

---

Author  
Mohamed Abdelrazek  
GitHub: https://github.com/MoeAbdelrazek  
LinkedIn: https://www.linkedin.com/in/moe-abdelrazek/  

---

Course Reference  
Programming in Python by Meta (Coursera):  
https://www.coursera.org/learn/programming-in-python
