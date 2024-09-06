

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_str = ""
    for s in string:
        if s.isupper():
            new_str += s.lower()
        elif s.islower():
            new_str += s.upper()
        else:
            new_str += s
    return new_str

