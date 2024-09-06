
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # begin_string = str(x)
    # shifted_string = ""
    # if shift > len(begin_string):
    #     return begin_string[::-1]
    # else:
    #     for i in range(shift):
    #         shifted_string += begin_string[-1]
    #         begin_string = begin_string[:-1]
    #     return shifted_string + begin_string
    return (str(x)[shift:] + str(x)[:shift])[::-1]


