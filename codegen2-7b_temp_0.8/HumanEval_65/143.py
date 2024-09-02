
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = ""
    for c in str(x):
        s += c
    s = s[shift:] + s[:shift]
    return s if len(s) < 10 else "0" * 9 + s[1:]

