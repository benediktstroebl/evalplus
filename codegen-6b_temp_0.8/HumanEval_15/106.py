

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # If you have a list of numbers, you can compute this using:
    # return ' '.join(map(str, range(n+1)))

    # ...
    # or
    # return ' '.join(map(str, range(n+1)))
    # ...
    
    # So now we can do it with strings.
    return ' '.join(map(str, range(n+1)))
