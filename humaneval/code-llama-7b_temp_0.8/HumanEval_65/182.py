
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
    if x == 0:
        return "0"
    if x < 0:
        negative = True
        x = -x
    else:
        negative = False
    str_x = str(x)
    digits = len(str_x)
    if shift >= digits:
        return str_x[::-1]
    shifted_x = str_x[shift:] + str_x[:shift]
    if negative:
        return "-" + shifted_x
    else:
        return shifted_x

