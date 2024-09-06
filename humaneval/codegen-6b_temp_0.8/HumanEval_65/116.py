
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert isinstance(x, int)
    assert isinstance(shift, int)
    shift %= len(str(x))
    if x > 0:
        return int(''.join(str(x)[shift:] + str(x)[:shift]))
    else:
        return int(''.join(str(x)[len(str(x))-shift:][::-1] + str(x)[:len(str(x))-shift]))

