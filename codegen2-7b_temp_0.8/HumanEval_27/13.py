

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    lowercase_text = string.lower()
    uppercase_text = string.upper()
    return uppercase_text + lowercase_text[1:]
