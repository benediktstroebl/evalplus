

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    # we use the range() function to generate a list of integers
    # (our_range = [0, 1, 2, 3, 4, 5])
    our_range = range(n + 1)

    # we use the join() function to turn a list into a string
    # (our_string = '0 1 2 3 4 5')
    our_string = " ".join(str(x) for x in our_range)

    return our_string

