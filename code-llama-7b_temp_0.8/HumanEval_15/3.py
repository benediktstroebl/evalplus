

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # 1st solution
    # return ' '.join(str(n) for n in range(n+1))
    # 2nd solution
    string = ''
    for n in range(n+1):
        string += str(n) + ' '
    return string[:-1]

