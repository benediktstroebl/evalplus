

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    # note that we can use a for loop to generate a list of numbers,
    # but strings are sequences too!
    sequence = " "
    for i in range(n+1):
        sequence += str(i) + " "
    return sequence

