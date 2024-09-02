

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # turn to list so it can be modified
    str_list = list(string)
    for idx, char in enumerate(string):
        if char.isupper():
            str_list[idx] = char.lower()
        else:
            str_list[idx] = char.upper()
    return ''.join(str_list)

