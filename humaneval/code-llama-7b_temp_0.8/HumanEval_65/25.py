
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
    for i in range(1, len(str(x)) + 1):
        num = x // (10 ** (i - 1)) % 10
        result += str(num)
        if i > shift:
            break
    return result[::-1]
