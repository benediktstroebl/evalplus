
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # count leading zeros in shift
    zeros = len(str(shift)) - len(str(int(shift) % 10))
    # adjust x to have leading zeros
    x = '0' * zeros + int(x)
    # shift x to the right
    x_shifted = x / 10 ** (len(str(int(x) % 10)) - zeros)
    return str(x_shifted)
