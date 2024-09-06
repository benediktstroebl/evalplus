
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
    def first_condition(file_name):
        return len(file_name) > 3 and file_name.count(".") == 1 \
               and file_name[0].isalpha() and file_name[1:].split(".")[0]

    def second_condition(file_name):
        splitted = file_name.split(".")
        return splitted[1] in ['txt', 'exe', 'dll']

    return first_condition(file_name) and second_condition(file_name)

assert file_name_check("example.txt") is True, "example.txt is a valid file name."
assert file_name_check("1example.dll") is False, "1example.dll is not a valid file name, because it starts with a latin alphapet letter."
assert file_name_check("ex2p.docx") is False, "ex2p.docx is not a valid file name, because it contains more than three digits, or it contains a dot."
assert file_name_check("x.txt") is False, "x.txt is not a valid file name, because it does not contain one dot."
assert file_name_check("1.txt") is False, "1.txt is not a valid file name, because it does not contain one dot."
assert file_name_check("example.exe") is True, "example.exe is a valid file name."
assert file_name_check("ex.exe") is True, "ex.exe is a valid file name."
assert file_name_check("zzz.exe") is False, "zzz.exe is not a valid file name, because it does not start with a latin alphapet letter."
assert file_name_check("a.exe") is False, "a.exe is not a valid file name, because it does not contain one dot."
assert file_name_check("1.exe") is False, "1.exe is not a valid file name, because it does not contain one dot."
assert file_name_check("a.exea") is False, "a.exea is not a valid file name, because it contains multiple dots."
assert file_name_check("a.exea.exe") is False