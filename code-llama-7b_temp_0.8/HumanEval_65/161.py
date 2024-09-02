
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # The number of digits of x
    length = len(str(x))

    # Convert x to a string
    x = str(x)

    # If shift is bigger than the number of digits of x,
    # we're just reversing the digits
    if shift >= length:
        return x[::-1]

    # Shift the digits to the right by shift
    return x[length - shift:] + x[:length - shift]
