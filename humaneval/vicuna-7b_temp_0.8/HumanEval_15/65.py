

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    n_str = ' '
    n_index = 0
    while n_index < n:
        n_str += str(n_index)
        n_index += 1
    return n_str