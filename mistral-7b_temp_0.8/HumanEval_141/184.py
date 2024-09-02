
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    def check_digits(name):
        for i in name:
            if i.isdigit():
                return i
            else:
                return name

    def check_first_letter(name):
        for i in name:
            if i.isalpha():
                return name
            else:
                return name

    def check_type(name):
        types = ('txt', 'exe', 'dll')
        for i in name:
            if i in types:
                return name
            else:
                return name

    def check_one_dot(name):
        for i in name:
            if i == '.':
                return name
            else:
                return name

    if check_digits(file_name) > 3:
        print("No")
    elif check_first_letter(file_name[0]) != file_name[0]:
        print("No")
    elif check_one_dot(file_name) == '':
        print("No")
    elif check_type(file_
