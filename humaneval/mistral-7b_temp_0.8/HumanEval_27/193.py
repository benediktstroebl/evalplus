

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    output = ""
    for char in string:
        if char.isupper():
            output += char.lower()
        else:
            output += char.upper()
    return output
