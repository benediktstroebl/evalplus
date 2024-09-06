
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    # x = list(str(x))
    # str_x = "".join(x)
    # print(x)
    # print(str_x)
    #
    # if shift >= len(x):
    #     x = str(x)
    #     return x[::-1]
    # else:
    #     return x[shift:] + x[:shift]

    str_x = str(x)
    str_x = str_x[shift:] + str_x[:shift]

    return str_x

