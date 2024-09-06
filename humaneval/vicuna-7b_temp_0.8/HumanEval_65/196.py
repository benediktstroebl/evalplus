
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Shift the digits right
    str_shift = '0' * (shift - len(str(x))) + str(x)
    # Reverse the string
    str_rev = str_shift[::-1]
    return str_rev
