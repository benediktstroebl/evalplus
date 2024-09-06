def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to `n` inclusive. """
    numbers = f'{n}{n + 1}'
    for i in range(2, n + 1):
        numbers += f' {i}'
    return numbers