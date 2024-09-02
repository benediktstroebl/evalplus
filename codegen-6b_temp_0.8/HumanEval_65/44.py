
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift > abs(x):
        return str(x)[::-1]
    s = str(x)
    return "".join(map(str, (int(s[i]) for i in range(len(s) - shift, len(s)) +
                             range(0, len(s) - shift))))

