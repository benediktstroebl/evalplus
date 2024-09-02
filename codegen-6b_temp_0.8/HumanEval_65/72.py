
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    num_digits = len(str(abs(x)))
    if shift > num_digits:
        return str(abs(x))[::-1]
    elif shift < 0:
        return str(abs(x))[(num_digits - shift):] + str(abs(x))[:num_digits - shift]
    else:
        return str(abs(x))[shift:] + str(abs(x))[:shift]

