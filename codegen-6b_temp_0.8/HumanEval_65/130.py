
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # TODO: Generalize the number of digits in the number x
    digits = len(str(x))
    if shift > digits:
        shift = (shift - digits) % digits
        new_x = x // 10**shift + x % 10**shift
    else:
        shift = shift % digits
        new_x = int(str(x)[shift:] + str(x)[:shift])
    return str(new_x)

