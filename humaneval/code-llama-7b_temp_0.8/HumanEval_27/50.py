

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    # solution 1
    # return "".join(c.swapcase() for c in string)

    # solution 2
    # return "".join(c.upper() if c.islower() else c.lower() for c in string)

    # solution 3
    # return string.swapcase()

    # solution 4
    # return string.upper() if string.islower() else string.lower()

    # solution 5
    return string.swapcase()
