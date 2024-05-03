class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the To-do list.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the To-do list.")
        else:
            print(f"Task '{task}' not found in the To-do list.")

    def view_tasks(self):
        if self.tasks:
            print("To-do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("To-do List is empty.")

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            print("Thank you for using the To-do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

