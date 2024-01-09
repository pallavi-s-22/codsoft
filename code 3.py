class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self):
        task_name = input("Enter the task name: ")
        task_particulars = input("Enter the task particulars ")
        self.tasks[task_name] = task_particulars
        print("Task added successfully!")

    def display_task(self):
        if self.tasks:
            print("Your To-Do List:")
            for task_name, task_particulars in self.tasks.items():
                print(f"Task: {task_name}\nParticulars: {task_particulars}\n")
        else:
            print("Your to-do list is empty.")

    def revise_task(self):
        task_name = input("Enter the task name you want to revise: ")
        if task_name in self.tasks:
            new_particulars = input("Enter the revised particulars: ")
            self.tasks[task_name] = new_particulars
            print("Task revised successfully!")
        else:
            print("Task not found.")

    def remove_task(self):
        task_name = input("Enter the task name you want to remove: ")
        if task_name in self.tasks:
            del self.tasks[task_name]
            print("Task removed successfully!")
        else:
            print("Task not found.")

    def menu(self):
        print("\nTo-Do List Table\n")
        print("1. Add Task")
        print("2. Display Task")
        print("3. Revise Task")
        print("4. Remove Task")
        print("5. Exit")
        option = input("Enter your choice from (1-5): ")
        return option

def add_task(todo):
    todo.add_task()

def display_task(todo):
    todo.display_task()

def revise_task(todo):
    todo.revise_task()

def remove_task(todo):
    todo.remove_task()

def run(todo):
    while True:
        option = todo.menu()
        if option == '1':
            add_task(todo)
        elif option == '2':
            display_task(todo)
        elif option == '3':
            revise_task(todo)
        elif option == '4':
            remove_task(todo)
        elif option == '5':
            print("You exited from your To Do list")
            break
        else:
            print("Invalid option. Please enter a valid option from the To Do List table.")

todo = ToDoList()
run(todo)