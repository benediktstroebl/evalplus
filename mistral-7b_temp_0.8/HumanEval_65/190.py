
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x_str = str(x)
    x_list = list(x_str)
    if shift <= len(x_list):
        x_list.append(x_list[0])
        x_list = x_list[:shift] + x_list[shift:]
        result_str = ''.join(x_list)
        return result_str
    else:
        return x_str[::-1]
