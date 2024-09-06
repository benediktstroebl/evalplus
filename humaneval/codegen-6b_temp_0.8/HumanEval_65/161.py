
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if len(str(x)) == shift:
        return str(x)
    elif len(str(x)) < shift:
        return "".join(str(x)[len(str(x))-shift:]) + "".join(str(x)[:len(str(x))-shift])
    else:
        return "".join(str(x)[-shift:]) + "".join(str(x)[:-shift])
