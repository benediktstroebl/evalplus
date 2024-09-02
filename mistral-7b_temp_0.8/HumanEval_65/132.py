
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # we should use the built-in function for this
    # return str(int(x / 10**shift) * 10**(n - shift) + x % 10**shift)
    str_x = str(x)
    if shift <= len(str_x):
        return str_x[-shift:] + str_x[:-shift]
    else:
        return str_x[-shift:] + str_x[:-shift]
