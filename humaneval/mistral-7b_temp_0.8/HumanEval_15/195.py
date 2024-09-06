

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # Make a string using concatenation and a list comprehension.
    # To concatenate strings, you can just add them together.
    # You can also use + or the * operator to add the same string multiple times.
    return ' '.join([str(i) for i in range(n + 1)])

