
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if x < 0:
        # For negative integers, get positive version,
        # shift right, and make negative again.
        return "-" + circular_shift(-x, shift)
    s = str(x)
    if shift > len(s):
        # Shift larger than string length: reverse string.
        return s[::-1]
    return s[len(s)-shift:] + s[:len(s)-shift]
