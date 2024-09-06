

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    numbers_string = ''
    for num in range(n+1):
        if num == 0:
            numbers_string += str(num)
        else:
            numbers_string += f' {num}'
    return numbers_string

