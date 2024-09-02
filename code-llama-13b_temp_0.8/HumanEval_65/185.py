
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
    length = len(str_x)
    if length <= 1:
        return str_x
    if shift >= length:
        shift %= length
    if shift == 0:
        return str_x
    str_x = list(str_x)
    temp = str_x[shift:length] + str_x[0:shift]
    result = ""
    for i in temp:
        result += i
    return result

