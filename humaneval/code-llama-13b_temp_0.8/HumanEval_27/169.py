

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Hint: Use str.islower() and str.isupper() to check if a character is in lowercase or uppercase.
    return string[::-1]

