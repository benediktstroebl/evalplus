

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    # base case
    if n < 0:
        return ''
    if n == 0:
        return '0'

    # recursive case
    first_half = string_sequence(n - 1)
    return first_half + ' ' + str(n)

