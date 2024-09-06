

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # first, handle special case of 0 and 1
    if n == 0:
        return "0"
    if n == 1:
        return "0 1"
    # otherwise, return the concatenation of string_sequence of each of the sub-problems
    else:
        return " ".join(string_sequence(i) for i in range(n))


