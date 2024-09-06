

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_string = string.upper()
    for i in range(0, len(string)):
        if new_string[i] in 'abcdefghijklmnopqrstuvwxyz':
            new_string = new_string[:i] + new_string[i].lower() + new_string[i + 1:]
    return new_string

