
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    number_of_digits = len(str(abs(x)))
    digits = str(x)
    if shift > number_of_digits:
        return str(int(digits[::-1]))
    # note that the slice notation [::1] does the same as [:], so the reverse
    # order is flipped
    return x + str(int(digits[-shift:] + digits[:-shift]))

