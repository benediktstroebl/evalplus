
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    sign = 1 if x < 0 else 0
    x = abs(x)
    result = str(x)
    while shift > 0:
        shift -= 1
        result = result[::-1] + result[1:]
    return sign + result[-shift:]
