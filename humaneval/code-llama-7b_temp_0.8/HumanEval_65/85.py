
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # x = int(x)
    # print(x)
    # if shift > len(str(x)):
    #     return str(x)[::-1]
    # elif x < 0:
    #     return str(-int(str(-x)[shift:] + str(-x)[:shift]))[::-1]
    # else:
    #     return str(int(str(x)[shift:] + str(x)[:shift]))

    s = str(x)[::-1]
    return s[:shift][::-1] + s[shift:]

