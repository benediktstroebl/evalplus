
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
    assert 0 <= shift < len(str(x))
    first_digits = x // 10 ** (len(str(x)) - shift)
    last_digits = x % 10 ** (len(str(x)) - shift)
    return str(last_digits) + str(first_digits)

