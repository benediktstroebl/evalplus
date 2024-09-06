

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    uppercase_string = ""
    for char in string:
        if char.islower():
            uppercase_string += char.upper()
        else:
            uppercase_string += char.lower()
    return uppercase_string
