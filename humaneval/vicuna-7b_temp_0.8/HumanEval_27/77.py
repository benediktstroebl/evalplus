

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = string.upper() + string[1:]
    for i in range(1, len(string)):
        if string[i] == string[0]:
            string = string[0] + string[i]
    return string
