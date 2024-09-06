def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to `n` inclusive. """
    numbers = f'{n}-{n}'
    return ' '.join(str(num) for num in range(int(numbers) + 1))