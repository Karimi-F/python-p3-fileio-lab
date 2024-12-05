def write_file(write_file, file_content):
    write_file = f"{write_file}.txt" 
    with open(write_file, 'w') as file:
        file.write(file_content)

def append_file(append_file, append_content):
    append_file = f"{append_file}.txt"
    with open(append_file, "a") as file:
        file.write(append_content)

def read_file(file_name):
    file_name = f"{file_name}.txt"
    with open (file_name, 'r') as file:
        return file.read()
