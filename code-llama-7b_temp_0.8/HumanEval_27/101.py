

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # We can make use of the str.swapcase() method.
    # When run on a string, this method capitalises all lowercase characters and
    #   small-caps all uppercase characters.
    return string.swapcase()

