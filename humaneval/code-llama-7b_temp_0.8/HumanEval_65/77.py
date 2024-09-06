
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert to a string, because we're treating it like one
    s = str(x)
    # Figure out how many times we need to rotate the digits
    shift = shift % len(s)
    # Rotate the digits and reverse the order
    return ''.join(reversed(s[shift:] + s[:shift]))
