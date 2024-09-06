

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    if n == 0:
        return "0"
    elif n == 1:
        return "0 1"
    elif n == 2:
        return "0 1 2"
    else:
        result = "0 "
        for i in range(1, n):
            result += str(i) + " "
        result += str(n)
        return result

