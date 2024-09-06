

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    count = 0
    res = ""
    while count < n:
        res += str(count) + " "
        count += 1
    return res[:-1]

