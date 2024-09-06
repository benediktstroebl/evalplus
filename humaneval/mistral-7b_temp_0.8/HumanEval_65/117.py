
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    result = ''
    while x > 0:
        n = x % 10
        result = n + result
        x = x // 10

    if shift > len(result):
        result = result[1:] + result[0]
    else:
        result = result[shift:] + result[:shift]
    return result
