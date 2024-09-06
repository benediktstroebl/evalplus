

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    # Create a variable to store the length of the string
    length = 0

    # Loop through the string
    for char in string:
        # Increment length for every character
        length += 1

    # Return the length
    return length

