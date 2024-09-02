

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # 1. BASE CASE: A string of length 0 contains no numbers.
    if n == 0:
        return '0'

    # 2. RECURSIVE STEP: Build a string with the next number in the sequence
    # by recursively solving a problem of one less than the target size.
    return string_sequence(n - 1) + ' ' + str(n)

