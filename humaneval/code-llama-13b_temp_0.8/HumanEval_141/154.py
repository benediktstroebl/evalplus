
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
    # if not file_name:
    #     return 'No'

    # flag = True

    # if not file_name[0].isalpha():
    #     flag = False

    # for i in file_name:
    #     if i.isdigit() and file_name.count(i) > 3:
    #         flag = False
    #         break

    # if '.' not in file_name or file_name.count('.') > 1:
    #     flag = False

    # if not file_name[-1].isdigit():
    #     flag = False

    # if file_name[-1].isdigit() and file_name[-2].isdigit():
    #     flag = False

    # sub_file_name = file_name.split('.')

    # if len(sub_file_name[1]) == 0:
    #     flag = False

    # if sub_file_name[1] not in ['txt', 'exe', 'dll']:
    #     flag = False

    # return 'Yes' if flag else 'No'

    # phone 0123 456 789
    # # 0123 456789
    # print(len(file_name))
    # digits_counter = 0
    # for digit in file_name:
    #     if digit.isdigit():
    #         digits_counter += 1
    # print(digits_counter)

    if not file_name:
        return 'No'

    for char in file_name:
        if char.isdigit() and file_name.count(char) > 3:
            return 'No'

    if file_name[0].isdigit() or file_name.count('.') != 1 or file_name[-1] == '.':
        return 'No'

    if not file_name[0].isalpha() or file_name[-1] == '.' or file_name[-1].isdigit():
        return 'No'

    for char in file_name:
        if char == '.' and (file_name
