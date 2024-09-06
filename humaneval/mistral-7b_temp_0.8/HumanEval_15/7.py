

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    def string_sequence_loop(n: int) -> str:
        if n == 0:
            return ""
        else:
            return str(n - 1) + " " + string_sequence_loop(n - 1)

    return string_sequence_loop(n)
