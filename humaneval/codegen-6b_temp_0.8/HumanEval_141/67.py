
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
    def file_name_checker(file_name):
        def ne_num_filter(s):
            return not any(c.isdigit() for c in s)

        def ne_dot_filter(s):
            return s.count(".") != 1 or s.count(".") == 1 and s.count(".") * 2 != len(s)

        def ne_start_filter(s):
            return s.count(".") == 1 and s.count(".") == 1 and (s[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' or s[1] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

        def ne_end_filter(s):
            return s.count(".") == 1 and s.count(".") == 1 and (s[-1] in 'exe dll txt' or s[-1] == '.')

        return 'Yes' if ne_num_filter(file_name) and ne_dot_filter(file_name) and ne_start_filter(file_name) and ne_end_filter(file_name) else 'No'

    return file_name_checker(file_name)

