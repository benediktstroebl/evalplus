

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    # sequences = '0 1 2 3 4 5'
    # spaces = ' '

    sequences = '0'
    spaces = ' '
    for number in range(1, n + 1):
        sequences = sequences + spaces + str(number)

    return sequences

