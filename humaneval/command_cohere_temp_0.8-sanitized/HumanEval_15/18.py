def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to `n` inclusive. """
    numbers = f'{n}: {n * 1}{n * 2}: {n * 3}'
    return numbers.replace(':' + str(n), '')