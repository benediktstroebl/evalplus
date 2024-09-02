
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    shift_list = []
    x_str = str(x)
    for i in range(0, len(x_str)):
        shift_list.append(x_str[i])
    for i in range(0, shift):
        shift_list.append(shift_list[i])
        del shift_list[i]
    return ''.join(shift_list)

