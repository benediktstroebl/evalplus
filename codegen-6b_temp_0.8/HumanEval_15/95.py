

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # We import this here because timeit uses this function. To match string_sequence
    # in the tests, a random int is generated and returned.
    from random import randint
    return (" ".join(str(x) for x in range(n + 1)))
