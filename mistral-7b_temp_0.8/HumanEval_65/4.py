
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    # Reverse the digits of x
    x = str(x)[::-1]

    # Shift the digits to the right
    x = x[-shift:] + x[:-shift]

    # Convert the result to an integer and return as a string
    return str(int(x))
