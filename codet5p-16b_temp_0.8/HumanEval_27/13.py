

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    string_list = list(string)
    for i in range(len(string)):
        if string_list[i].islower():
            string_list[i] = string_list[i].upper()
        else:
            string_list[i] = string_list[i].lower()
    return ''.join(string_list)

