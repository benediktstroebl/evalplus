
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    """
    method 1:
    x_str = str(x)
    len_x = len(x_str)

    if shift > len_x:
        return x_str[::-1]
    else:
        return x_str[shift:] + x_str[:shift]
    """

    """
    method 2:
    str_x = str(x)
    len_x = len(str_x)
    shift %= len_x
    shift_first = str_x[:shift]
    shift_last = str_x[shift:]
    return shift_last + shift_first
    """

    """
    method 3:
    """
    str_x = str(x)
    len_x = len(str_x)
    shift %= len_x
    return str_x[shift:] + str_x[:shift]

