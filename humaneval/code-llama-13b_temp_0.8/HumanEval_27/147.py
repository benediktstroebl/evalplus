

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_str = ""
    for char in string:
        if char.isupper():
            new_str += char.lower()
        else:
            new_str += char.upper()
    return new_str

