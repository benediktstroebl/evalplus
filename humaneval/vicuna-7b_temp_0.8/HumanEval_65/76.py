
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = "0"
    while shift > 0:
        if x % 10 == 0:
            s = s + str(x // 10)
            x = x % 10
            shift -= 1
        x = x // 10
        shift -= 1
    return s + str(x)
