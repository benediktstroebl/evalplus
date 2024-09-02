
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert to a string and reverse it
    x = str(x)
    x = x[::-1]

    # Reverse the result if shift > number of digits
    if shift > len(x):
        x = x[::-1]

    # Add zero to the beginning of the string if shift < 0
    elif shift < 0:
        x = '0' + x

    # Circularly shift the result by shift
    elif shift > 0:
        x = x[shift:] + x[:shift]

    return x

