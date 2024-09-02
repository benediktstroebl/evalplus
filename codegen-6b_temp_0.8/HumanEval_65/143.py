
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    shift %= len(str(x))
    x_list = list(str(int(x)))
    # reverse list if shift is greater than length of list
    if shift > len(x_list):
        x_list.reverse()
    elif shift < 0:
        x_list = x_list[shift:] + x_list[:shift]
    else:
        x_list = x_list[shift:] + x_list[:shift]
    return ''.join(x_list)

