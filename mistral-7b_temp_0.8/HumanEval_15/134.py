

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # First test if n is negative or not
    if n < 0:
        return ""
    # Initialize the sequence
    sequence = ""
    # Initialize the number
    number = 0
    # Create the sequence
    while number <= n:
        sequence += str(number)
        sequence += " "
        number += 1
    # Return the sequence
    return sequence
