
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift == 0:
        return str(x)
    # convert to string
    x = str(x)
    # get length of string
    n = len(x)
    # get rightmost digits
    rightmost_digits = x[n-shift:n]
    # get leftmost digits
    leftmost_digits = x[:n-shift]
    # get middle digits
    middle_digits = x[n-shift:n]
    # reverse middle digits
    middle_digits = middle_digits[::-1]
    # return leftmost + middle + rightmost digits
    return leftmost_digits + middle_digits + rightmost_digits
