
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # convert the integer to a string
    x_string = str(x)
    # The number of digits of the integer x
    num_digits = len(x_string)
    # The shifted integer
    x_shifted = x_string[num_digits - shift:] + x_string[:num_digits - shift]
    return x_shifted
