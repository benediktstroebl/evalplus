

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_str = ''
    for i in string:
        if i.isupper():
            new_str += i.lower()
        elif i.islower():
            new_str += i.upper()
        else:
            new_str += i
    return new_str

