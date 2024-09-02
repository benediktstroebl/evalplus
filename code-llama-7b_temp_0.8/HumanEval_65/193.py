
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
    num_len = len(str_num)
    shift = shift % num_len
    if shift > num_len:
        return str_num[::-1]
    else:
        return str_num[shift:] + str_num[:shift]

