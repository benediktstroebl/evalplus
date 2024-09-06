
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x = int(x)
    x_str = str(x)
    if len(x_str) == 1:
        return x_str
    x_str_list = list(x_str)
    for i in range(shift):
        x_str_list = [x_str_list[-1]] + x_str_list[:-1]
    return "".join(x_str_list)

