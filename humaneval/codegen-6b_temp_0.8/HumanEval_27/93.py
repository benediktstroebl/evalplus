

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # return string.swapcase()
    new_string = ""
    for s in string:
        if s.isupper():
            new_string += s.lower()
        elif s.islower():
            new_string += s.upper()
        else:
            new_string += s
    return new_string
