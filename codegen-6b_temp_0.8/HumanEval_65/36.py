
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    diff = abs(shift)
    if diff >= len(str(x)):
        return str(x)[::-1]

    return str(int(str(x)[:len(str(x)) - diff] + str(x)[len(str(x)) - diff + 1:]))
