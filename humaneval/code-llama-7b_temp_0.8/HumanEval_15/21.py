

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    #---------------------------------------------------------------------------
    # This is an example of a "repetition" pattern, which produces a list of
    # n numbers from 0 to n-1.  You can use it to generate sequences of numbers.
    #---------------------------------------------------------------------------
    return ' '.join(str(i) for i in range(n))

