

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    result = ''
    for i in range(n):
        result += str(i)
    return result

@number_rule(
    description='Validate whether the number is a prime number',
    validate=lambda x: x > 0 and x % 2 == 1 and x % 3 == 0,
    evaluate=lambda x: x == 2 or string_sequence(x - 1),
)
