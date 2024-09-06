def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive. """
    numbers = f'{n}: {n * 2}'[::-1].replace(': ', ' to ')
    return f'0 {numbers}' if n else '0'