

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string_flipped = ''
    for char in string:
        if char.isupper():
            string_flipped += char.lower()
        else:
            string_flipped += char.upper()
    return string_flipped
