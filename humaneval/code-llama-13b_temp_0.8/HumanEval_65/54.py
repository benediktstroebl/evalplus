
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x_string = str(x)
    x_length = len(x_string)
    if shift <= x_length:
        x_list = list(x_string)
        x_list = x_list[shift:x_length] + x_list[0:shift]
        return "".join(x_list)
    else:
        return x_string[::-1]
