
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # print(x)
    # print(type(x))
    # print(x.bit_length())
    # digits = str(x)
    # if len(digits) <= shift:
    #     return digits[::-1]
    # return digits[shift:] + digits[:shift]
    if len(str(x)) <= shift:
        return str(x)[::-1]
    return str(x)[shift:] + str(x)[:shift]

