
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = "0" + str(x)
    while len(digits) > 0:
        digit = digits[:-1]
        if len(digit) > 1:
            # handle right shift
            x = (x // digit) + (x % digit)
        else:
            # handle left shift
            x = (x // digit) + (x % 10)
        digits = digit + str(x)
    if shift > len(digits):
        return digits[::-1]
    return digits
