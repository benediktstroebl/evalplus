

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_string = []
    for char in string:
        if char.isupper():
            new_string.append(''.join(map(lambda x: x.lower(), char)))
        elif char.islower():
            new_string.append(''.join(map(lambda x: x.upper(), char)))
        else:
            new_string.append(char)
    return ''.join(new_string)

