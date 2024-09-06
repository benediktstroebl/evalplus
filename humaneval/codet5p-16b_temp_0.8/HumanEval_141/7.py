
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

    assert file_name.count('.') == 1, 'Too many dots.'
    if file_name.count('0') + file_name.count('1') + file_name.count('2') + file_name.count('3') + file_name.count('4') + file_name.count('5') + file_name.count('6') + file_name.count('7') + file_name.count('8') + file_name.count('9') > 3, 'Too many digits.'
    assert file_name.find('.') == 0, 'The file name should start with a latin alphapet letter.'
    assert file_name.find('a') >= 0 or file_name.find('A') >= 0 or file_name.find('z') >= 0 or file_name.find('Z') >= 0, 'The substring before the dot should not be empty, and it starts with a latin alphapet letter.'
    assert file_name.find('txt') >= 0 or file_name.find('exe') >= 0 or file_name.find('dll') >= 0,
