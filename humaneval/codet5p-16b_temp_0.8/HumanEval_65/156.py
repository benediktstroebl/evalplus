
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    shift = shift % len(str(x))
    s = str(x)
    return (s[-shift:] + s[:-shift]) if shift else s[::-1]
    
