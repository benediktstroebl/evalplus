

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    # The sequence of the conditions matters
    # We want to check for uppercase before lowercase
    return ''.join(
        c.upper() if c.islower() else c.lower()
        for c in string
    )

