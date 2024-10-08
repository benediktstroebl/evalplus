
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    """
    if len(str(x)) > shift:
        str_x = str(x)
        return str_x[shift:] + str_x[:shift]
    return str(x)[::-1]
    """
    str_x = str(x)
    if len(str_x) > shift:
        return str_x[shift:] + str_x[:shift]
    return str(x)[::-1]
    
    #return ""

