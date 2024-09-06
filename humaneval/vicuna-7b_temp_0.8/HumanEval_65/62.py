
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # handle negative shift
    if shift < 0:
        shift = abs(shift)
        x = -x
    # handle overflow and underflow
    if x < 0:
        if -x >= 0:
            return "0"
        else:
            return "-" + str(abs(x))
    elif x >= 10:
        if x - 10 >= 0:
            return str(x - 10)
        else:
            return "0" + str(abs(x-10))
    # handle circular shift
    result = ""
    for i in range(0, len(str(x))):
        result += str(x[:i])
    for i in range(shift-1, len(str(x))-shift):
        result += "0"
    for i in range(shift-1, len(str(x))-shift):
        result += str(x[i:i+shift])
    return result