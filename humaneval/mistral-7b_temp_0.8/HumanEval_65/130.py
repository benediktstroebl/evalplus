
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # remove leading 0
    x = x % 10**9
    x = int(str(x)[::-1])
    digits = len(str(x))
    shift = shift % digits
    if shift == 0:
        return str(x)
    if shift > digits:
        shift = shift % digits
    return str(x)[shift:] + str(x)[0:shift]
