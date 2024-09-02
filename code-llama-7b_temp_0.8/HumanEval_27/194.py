

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    # Change all letters to uppercase
    uppercase_string = string.upper()

    # Change all letters to lowercase
    lowercase_string = uppercase_string.lower()

    return lowercase_string
