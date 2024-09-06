

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    if not string:
        return string

    new_string = []

    for char in string:
        if char.islower():
            new_string.append(char.upper())
        elif char.isupper():
            new_string.append(char.lower())
        else:
            new_string.append(char)

    return ''.join(new_string)

