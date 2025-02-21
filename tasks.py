def execute_task(task):
    if task['category'] == 'Email':
        return execute_email_task(task)
    elif task['category'] == 'File':
        return execute_file_task(task)
    elif task['category'] == 'To-Do':
        return execute_todo_task(task)
    else:
        return "Unknown Task Category"

def execute_email_task(task):
    # Simulate email sorting functionality
    return f"Executed Email Sorting Task: {task['description']}"

def execute_file_task(task):
    # Simulate file management functionality
    return f"Executed File Management Task: {task['description']}"

def execute_todo_task(task):
    # Simulate generic to-do task functionality
    return f"Executed To-Do Task: {task['description']}"
