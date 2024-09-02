
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    n = len(str(x))
    r = ''
    for i in range(n, -1, -1):
        r = str(int(r) * 10 + (x % 10)) + r
        x = x // 10
    return r[::-1] if n > shift else r
