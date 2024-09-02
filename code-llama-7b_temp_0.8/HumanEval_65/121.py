
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    str_num = str(x)
    if len(str_num) >= shift:
        return str_num[shift:] + str_num[:shift]
    else:
        str_num = str_num[::-1]
        return str_num[:shift] + str_num[shift:]


