

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # The answer is a string with a length of n+1.
    # To create a string of length n+1, we can use the "n*" operator.
    # We can use the "join" function to join the string " " n+1 times.
    # We can use the "range" function to create a range from 0 to n.
    # We can use the "str" function to convert an integer to a string.
    return " ".join(str(i) for i in range(n+1))

