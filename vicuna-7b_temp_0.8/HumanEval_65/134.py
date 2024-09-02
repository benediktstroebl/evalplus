
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
    s = ''
    for i in range(n):
        if i < shift:
            s += str(x % 10)
        x = x // 10
        s += str(x % 10)
    if shift > n:
        s += str(x)
    return s
