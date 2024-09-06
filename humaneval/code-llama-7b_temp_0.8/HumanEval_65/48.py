
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert x to a string
    s = str(x)
    # If shift is greater than the number of digits, reverse the string
    if shift > len(s):
        s = s[::-1]
        return s
    else:
        s = s[shift:] + s[:shift]
        return s
