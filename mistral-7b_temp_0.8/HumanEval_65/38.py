
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = []
    while x > 0:
        s.append(x % 10)
        x = x // 10
    result = [i for i in s[shift:] + s[:shift]]
    return ''.join(map(str, result))
