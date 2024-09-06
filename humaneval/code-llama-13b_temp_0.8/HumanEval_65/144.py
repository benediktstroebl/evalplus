
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # convert integer to string
    x_str = str(x)
    # number of digits in x
    number_of_digits = len(x_str)
    # number of digits to shift
    # if shift is greater than number of digits,
    # shift by the number of digits
    shift = shift % number_of_digits or number_of_digits
    # return x_str[shift:] + x_str[:shift]
    return x_str[shift:] + x_str[:shift]

