
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # convert x into a string
    # reverse that string
    # shift the reversed string
    # reverse that string and return
    str_x = str(x)
    str_rev = str_x[::-1]
    str_rev_shift = str_rev[shift:]+str_rev[0:shift]
    return str_rev_shift[::-1]

