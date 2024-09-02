
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # x // 10 checks if there are any digits left
    # in the integer.
    # x % 10 gives the last digit.
    # s is a string of the last digit.
    s = str(x % 10)
    while x // 10:
        x = x // 10
        s = str(x % 10) + s
    # shifting the digits to the right
    return s[shift:] + s[:shift]

