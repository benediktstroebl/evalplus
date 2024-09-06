

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    s = string.upper()
    for char in string:
        if char.islower():
            s = s.replace(char, char.capitalize())
        elif char.isupper():
            s = s.replace(char, char.lower())
    return s
