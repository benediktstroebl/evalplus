
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    n = str(x)
    l = len(n)
    if l == 0:
        return "0"
    elif l < shift:
        return n[::-1]
    else:
        return n[shift:] + n[:shift]

