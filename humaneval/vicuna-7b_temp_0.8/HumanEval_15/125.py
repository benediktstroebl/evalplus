

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # Evaluate the recursive case (n == 0)
    if n == 0:
        return '0'
    # Evaluate the recursive case (n == 1)
    elif n == 1:
        return '0'
    # Use the recursive case as the initial case and apply the principle of mathematical induction
    else:
        return '{} {}'.format(string_sequence(n - 1), n)