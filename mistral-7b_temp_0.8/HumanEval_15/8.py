

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # 5.6) Write a function that takes an integer and returns a space-delimited string of
    #  integers starting at 0 upto the given integer inclusive.
    if n < 0:
        return 'Error: cannot count down from negative numbers.'
    return ' '.join(map(str, range(n + 1)))

