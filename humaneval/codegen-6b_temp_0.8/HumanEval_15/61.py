

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    t = ""
    for i in range(n + 1):
        t += str(i) + " "
    return t[:-1]  # don't forget to remove the last space!

