
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    assert type(x) == int and type(shift) == int, "Input must be integers"
    assert shift >= 0, "Shift must be non-negative"
    digits = list(str(x))
    digits.reverse()
    if shift >= len(digits):
        digits.reverse()
    else:
        digits = digits[shift:] + digits[:shift]
    digits.reverse()
    return ''.join(digits)

