

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    res = ""
    for i in range(len(string)):
        if string[i].isupper():
            res += string[i].lower()
        else:
            res += string[i].upper()
    return res

