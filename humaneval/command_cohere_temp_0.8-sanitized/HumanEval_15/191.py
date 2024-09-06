def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to `n` inclusive. """
    numbers = f'{n}-{n+1}'
    return f'0 {numbers[:-1]}' if n else '0'