
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    sign = 1 if x < 0 else -1
    x = sign * int(x)
    y = 0
    while x > 0:
        y = x % 10
        x = x // 10
    return str(int(y + (shift - len(str(y))) % 10))