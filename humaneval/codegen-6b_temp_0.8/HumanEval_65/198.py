
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert x > 0, "Input must be a positive integer."
    assert 0 <= shift <= len(str(x)), "Shift must be between 0 and number of digits."
    str_digits = str(x)
    shifted_digits = (str_digits[len(str_digits)-shift:] +
                      str_digits[:len(str_digits)-shift])
    return shifted_digits
