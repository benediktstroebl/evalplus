
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    #return str(int(str(x)[shift:] + str(x)[:shift]))

    digits = list(str(x))
    new_shift = shift % len(digits)
    digits = digits[new_shift:] + digits[:new_shift]
    return "".join(digits)
