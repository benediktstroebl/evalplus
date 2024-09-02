

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = string.upper() + string[1:]
    for i in range(len(string) - 1):
        if string[i] in string[i + 1].upper():
            string = string[0:-1] + string[-1].upper() + string[1:]
            break
    return string