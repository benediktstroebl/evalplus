

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    temp = ""
    for i in string:
        if i.isupper():
            temp = temp + i.lower()
        else:
            temp = temp + i.upper()
    return temp

