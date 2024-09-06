

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # return string.swapcase()
    # return "".join([c.upper() if c.islower() else c.lower() for c in string])

    return "".join(
        c.upper() if c in string.lower() else c.lower()
        for c in string
    )
