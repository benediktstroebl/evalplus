
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    strx = str(x)
    if shift > len(strx):
        return strx[::-1]
    else:
        strx_left = strx[:len(strx)-shift]
        strx_right = strx[len(strx)-shift:]
        return strx_right+strx_left

