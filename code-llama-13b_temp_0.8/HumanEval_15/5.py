

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    output_string = ''

    for number in range(n + 1):
        output_string = output_string + str(number) + ' '

    return output_string[:-1]
