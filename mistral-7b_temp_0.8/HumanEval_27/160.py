

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = string.lower()
    for char in string:
        if char.isupper():
            string = string.replace(char, char.lower())
        else:
            string = string.replace(char, char.upper())
    return string

