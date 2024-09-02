

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    # this will eventually be a string
    sequence = ''
    # for each number, starting from 0 up to n
    for i in range(n + 1):
        # if this is not the first number, add a space before it
        if sequence != '':
            sequence += ' '
        # add this number to the string
        sequence += str(i)

    return sequence

