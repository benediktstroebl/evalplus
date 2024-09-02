

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_str = ""
    for letter in string:
        if letter.isupper():
            new_str += letter.lower()
        else:
            new_str += letter.upper()
    return new_str
