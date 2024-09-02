
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # convert to a string
    string_x = str(x)
    # check for a negative shift
    if shift < 0:
        shift = len(string_x) + shift
    # check for a shift greater than the number of digits
    if shift >= len(string_x):
        return string_x[::-1]
    # check for a shift less than the number of digits
    elif shift == 0:
        return string_x
    else:
        return string_x[-shift:] + string_x[:-shift]

