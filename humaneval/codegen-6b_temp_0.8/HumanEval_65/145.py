
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert integer x to a string and shift its string digits
    x = str(x)
    return x[-shift:] + x[:-shift] if shift > len(x) else x[shift:] + x[:shift]

