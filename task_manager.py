import datetime

# Task class to encapsulate task details and operations
class Task:
    def __init__(self, task_id, description, due_date, priority, status='pending'):
        self.task_id = task_id
        self.description = description
        self.due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d')
        self.priority = priority
        self.status = status

    def __repr__(self):
        return f"ID: {self.task_id}, Description: {self.description}, Due: {self.due_date.date()}, Priority: {self.priority}, Status: {self.status}"

# TaskManager class to manage task operations
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description, due_date, priority):
        task = Task(self.next_id, description, due_date, priority)
        self.tasks.append(task)
        self.next_id += 1
        print("Task added successfully.")

    def view_tasks(self, filter_status=None, sort_by=None):
        tasks_to_view = self.tasks
        if filter_status:
            tasks_to_view = [task for task in tasks_to_view if task.status == filter_status]

        if sort_by == 'due_date':
            tasks_to_view.sort(key=lambda x: x.due_date)
        elif sort_by == 'priority':
            tasks_to_view.sort(key=lambda x: x.priority)
        elif sort_by == 'status':
            tasks_to_view.sort(key=lambda x: x.status)

        for task in tasks_to_view:
            print(task)

    def update_task(self, task_id, description=None, due_date=None, priority=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if description:
                    task.description = description
                if due_date:
                    task.due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d')
                if priority:
                    task.priority = priority
                if status:
                    task.status = status
                print("Task updated successfully.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully.")

def main():
    manager = TaskManager()

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority level: ")
            manager.add_task(description, due_date, priority)
        elif choice == '2':
            filter_status = input("Enter status to filter (pending/completed) or press enter to skip: ")
            sort_by = input("Sort by (due_date/priority/status) or press enter to skip: ")
            manager.view_tasks(filter_status or None, sort_by or None)
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            description = input("Enter new description or press enter to skip: ")
            due_date = input("Enter new due date (YYYY-MM-DD) or press enter to skip: ")
            priority = input("Enter new priority level or press enter to skip: ")
            status = input("Enter new status (pending/completed) or press enter to skip: ")
            manager.update_task(task_id, description or None, due_date or None, priority or None, status or None)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
