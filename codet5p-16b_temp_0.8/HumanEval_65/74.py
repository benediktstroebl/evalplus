
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
    if shift > len(x):
        result = x[::-1]
    else:
        for i in range(len(x)):
            if i+shift > len(x):
                result += str(x[i+shift-len(x)])
            else:
                result += str(x[i+shift])
    return result

