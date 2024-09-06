

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    flip_str = ""
    for i in range(len(string)):
        if string[i].isupper():
            flip_str += string[i].lower()
        else:
            flip_str += string[i].upper()
    return flip_str

