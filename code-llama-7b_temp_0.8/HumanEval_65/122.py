
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    result = ""
    shift_str = str(shift)
    str_x = str(x)
    shift_int = int(shift_str)
    if shift_int > len(str_x):
        shift_int = len(str_x)
    return str_x[shift_int:] + str_x[:shift_int]

