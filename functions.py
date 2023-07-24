FILEPATH = "todos.txt"


def get_todo(filename=FILEPATH):
    with open(filename, "r") as file:
        read_todos = file.readlines()
    return read_todos


def write_todo(todo_args, filename=FILEPATH):
    with open(filename, "w") as file:
        file.writelines(todo_args)


def convert(feet, inches):
    meters = int(feet)*0.3048 + int(inches)*0.0254
    return meters

