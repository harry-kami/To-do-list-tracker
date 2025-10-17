# Project descripton 
# This is a simple CLI application that allows a user to keep track of tasks

# Ver 1. 
# This version should allow the user to add, delete, and view tasks

# Ver 2. (improve)
# This version should allow a user to mark a task as done or not, and view completed and uncompleted tasks
# Add JSON file integration from Roadmap.sh requirements

# Ver 1

tasks = []

# Functions

def view_tasks(): # View tasks
    #print("\n")
    global tasks
    if not tasks:
        print("There are currently no tasks.")
    else:
        print("Tasks📋    ")
        print("-----------------------------------------------")
        # Buggy code
        #i = 0
        #for task in tasks:
        #   i += 1
        # add an iterator to the for loop and make it print corresponding numbers in ascending order for each task
        #    print(f"{i}. {task}")
        
        index = 1
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("-----------------------------------------------")

def add_task(): # add new task
    #print("\n")
    print("Adding new task📝")
    new_task = input("Enter task: ")
    tasks.append(new_task)
    print(f"Task added✅ '{new_task}'.")

def delete_task(): # delete a task
    view_tasks() # show tasks before prompting for deletion
    try:
        #print("\n") 
        task_to_delete = int(input("Select task no. to delete: ")) - 1 # (minus the index position by 1 so it aligns with the task number)
        if task_to_delete >= 0 and task_to_delete < len(tasks):
            tasks.pop(task_to_delete)
            print(f"Task {task_to_delete + 1} has been deleted.")
        else:
            print(f"Task #{task_to_delete} was not found")
    except:
        print("Error! Invalid input")

# main code
def view_options(): # options pane
    #print("\n")
    print("Pick an option to proceed")
    print("-----------------------------------------------")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Exit")

print("--------- Welcome to the Task Tracker ---------")
while True:
    view_options() # loads options pane

    user_input = input("Select option (1,2,3,4) -> ")

    if user_input == "1":
        view_tasks() # calls view tasks function
    elif user_input == "2":
        add_task() 
    elif user_input == "3":
        delete_task() # *finish up code for delete task function
    elif user_input == "4":
        print("Exiting Task Tracker...👋")
        break
    else:
        print("Error! Invalid input")