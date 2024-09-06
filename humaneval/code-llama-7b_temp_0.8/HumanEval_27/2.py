

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    new_str = ""
    for char in string:
        if char.islower():
            char = char.upper()
        if char.isupper():
            char = char.lower()
        new_str += char

    return new_str
