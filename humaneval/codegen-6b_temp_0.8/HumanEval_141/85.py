
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
    def check_if_file_name_is_valid(file_name):
        def is_valid(file_name):
            is_valid = True
            for character in file_name:
                if character.isdigit():
                    is_valid = False
            return is_valid
        def is_valid_dot(file_name):
            return file_name.count('.') == 1
        def is_valid_substring_before_and_after(file_name):
            valid_substring_before = False
            valid_substring_after = False
            for character in file_name:
                if character.isalpha():
                    valid_substring_before = True
                if character.isdigit():
                    valid_substring_after = True
            return valid_substring_before and valid_substring_after
        call_valid_file_name = is_valid(file_name) and is_valid_dot(file_name) and is_valid_substring_before_and_after(file_name)
        return 'Yes' if call_valid_file_name else 'No'
    return check_if_file_name_is_valid(file_name)
