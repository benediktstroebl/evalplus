
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert isinstance(shift, int), "Shift must be an integer"
    assert shift >= 0, "Cannot have negative shifts"
    str_num = str(x)
    width = len(str_num)
    if shift > width:
        str_num = str_num[-1] * (width + 1)
    else:
        str_num = "0" * (width - shift) + str_num[-shift:] + "0" * shift
    return str_num

