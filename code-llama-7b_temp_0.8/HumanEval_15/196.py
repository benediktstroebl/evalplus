

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    # 1. BASE CASE: Return 0 if n is zero
    if n == 0:
        return '0'

    # 2. RECURSIVE CASE: call the function with n - 1 and add a space and n to the returned string
    else:
        return string_sequence(n - 1) + ' ' + str(n)

