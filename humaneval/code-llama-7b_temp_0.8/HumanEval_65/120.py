
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # result = ''
    # digits = str(x)
    # if len(digits) <= shift:
    #     result = digits[::-1]
    # else:
    #     result = digits[shift:] + digits[:shift]
    # return result
    return str(x)[shift % len(str(x)):] + str(x)[:shift % len(str(x))]
