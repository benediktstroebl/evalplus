
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
    if len(file_name) > 3:
        return "No"
    else:
        if file_name.count(".")!= 1:
            return "No"
        else:
            string_1, string_2 = file_name.split(".")
            if string_1.startswith("0") or string_1.startswith("1") or string_1.startswith("2") or string_1.startswith("3") or string_1.startswith("4") or string_1.startswith("5") or string_1.startswith("6") or string_1.startswith("7") or string_1.startswith("8") or string_1.startswith("9"):
                return "No"
            elif string_2.startswith("0") or string_2.startswith("1") or string_2.startswith("2") or string_2.startswith("3") or string_2.startswith("4") or string_2.startswith("5") or string_2.startswith("6") or string_2.startswith("7") or string_2.startswith("8") or string_2.startswith("9"):
                return "No"
            elif string_2 == "exe" or string_2 == "dll" or string_2 == "txt":
                return "Yes"
            else:
                return "No"
