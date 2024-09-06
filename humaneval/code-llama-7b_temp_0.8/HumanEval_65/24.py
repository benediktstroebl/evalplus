
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    num_str = str(x)
    num_str_list = list(num_str)

    if shift >= len(num_str):
        num_str_list.reverse()
        num_str = ''.join(num_str_list)
    else:
        new_list = num_str_list[shift:]
        new_list.extend(num_str_list[0:shift])
        num_str = ''.join(new_list)

    return num_str
