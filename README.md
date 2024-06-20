# Task-manager-python

A command-line task management system implemented in Python. This system allows users to add, remove, update, and view tasks with various attributes.

## Features

- **Create Task**: Add a new task with a description, due date, and priority level.
- **View Tasks**: Display all tasks with options to filter by status (pending/completed) and sort by due date, priority, or status.
- **Update Task**: Modify task details such as description, due date, priority, and status.
- **Delete Task**: Remove a task by its ID.

## Task Attributes

- **Task ID**: Unique identifier for each task.
- **Description**: A brief description of the task.
- **Due Date**: The deadline for the task (format: YYYY-MM-DD).
- **Priority**: The importance level of the task.
- **Status**: The current status of the task (pending/completed).

## Usage

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/task-manager.git
   cd task-manager
   
## DETAILED EXLANATION OF CHOICES MADE:

### Task Class

- **Attributes**: Each task has an ID, description, due date, priority, and status to fully describe it.
- **Initialization**: We use `datetime` for due dates to easily handle and compare dates.
- **Representation**: The `__repr__` method makes tasks easy to read when printed.

### TaskManager Class

- **Storage**: Tasks are kept in a list for easy management and iteration.
- **ID Management**: `next_id` ensures each task gets a unique ID.
- **CRUD Methods**: Separate methods for adding, viewing, updating, and deleting tasks keep the code organized and the functionality clear.

### Main Function

- **User Interface**: A simple command-line menu lets users interact with the system easily.
- **Input Handling**: Prompts gather the necessary information for each task operation.
- **Loop**: The program runs in a loop, allowing continuous use until the user decides to exit.
