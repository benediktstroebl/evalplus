
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # convert x to a tuple of digits
    digits = [int(d) for d in str(x)]
    # shift the digits right
    for i in range(shift):
        digits.insert(0, digits.pop())
    # convert the tuple back to a string and return
    return ''.join(str(d) for d in digits)