
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
    x_len = len(x_str)
    shift_str = str(shift)
    shift_len = len(shift_str)
    result = ''
    if shift_len == 1:
        if shift > x_len:
            for i in x_str:
                result = i + result
        else:
            for i in x_str:
                result = result + i
            result = result[shift:] + result[:shift]
    else:
        return "Error"
    return result

