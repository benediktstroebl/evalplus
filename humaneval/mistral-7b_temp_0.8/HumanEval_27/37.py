

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    output = ''
    for char in string:
        if char.islower():
            output += char.upper()
        else:
            output += char.lower()

    return output




