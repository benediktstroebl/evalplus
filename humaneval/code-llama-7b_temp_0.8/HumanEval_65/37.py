
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift < 0:
        return x
    else:
        str_x = str(x)
        length = len(str_x)
        new_x = str_x[-shift:] + str_x[:-shift]
        if length == len(new_x):
            return str(int(new_x[::-1]))
        else:
            return new_x
