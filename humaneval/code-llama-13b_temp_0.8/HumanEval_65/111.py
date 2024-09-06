
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
    num_digits = len(str_x)
    if shift > num_digits:
        return str_x[::-1]
    else:
        first_part = str_x[shift:]
        second_part = str_x[:shift]
        return first_part + second_part

