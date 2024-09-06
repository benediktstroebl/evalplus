
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if type(shift) != int:
        raise TypeError('shift must be an integer')
    if type(x) != int:
        raise TypeError('x must be an integer')
    if x < 0:
        raise ValueError('x must be positive')

    s = str(x)
    if shift < len(s):
        s = s[shift:] + s[:shift]
    return s[::-1]

