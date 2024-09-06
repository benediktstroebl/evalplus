
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # This solution uses Python's builtin reversed, and its own str function
    # which does a circular shift on a string, rather than the more obvious
    # [::-1]. It is not as elegant (as it would be), but is a bit cooler
    # since it does not require a chained list.
    length = len(str(x))
    if shift > length:
        return str(x)
    else:
        return str(int(str(x)[length - shift:] + str(x)[0:length - shift]))

