def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to `n` inclusive. """
    numbers = range(n+1)
    return ' '.join(map(str, numbers))