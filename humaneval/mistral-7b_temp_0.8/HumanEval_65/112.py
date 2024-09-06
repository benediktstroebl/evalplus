
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    str_x = str(x)
    str_x_list = list(str_x)
    for i in range(shift):
        str_x_list.append(str_x_list[0])
        str_x_list.pop(0)
    return "".join(str_x_list)
