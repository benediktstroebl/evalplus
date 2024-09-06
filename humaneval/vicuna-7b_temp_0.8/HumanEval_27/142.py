

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = string.upper() + string[1:]  # flip uppercase to lowercase
    string = string.lower() + string[:1]  # flip lowercase to uppercase
    return string
