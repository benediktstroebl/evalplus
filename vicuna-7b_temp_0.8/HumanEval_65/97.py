
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    mask = 10**shift
    result = 0
    while x:
        i = 0
        while x >= 10**shift and i < shift:
            result += x % 10
            x = x // 10
            i += 1
        result += x // 10
        x = x % 10
    return result * mask + (x << shift) & mask
