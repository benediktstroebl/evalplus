def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to `n` inclusive. """
    numbers = f'{n}: {n * 2 - 1}'
    return ' '.join(map(str, range(int(n), 0, -1))) + ' ' + numbers