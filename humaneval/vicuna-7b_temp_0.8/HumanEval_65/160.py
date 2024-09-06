
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    y = "0" * len(str(x))
    i = 0
    while x != 0:
        if x % 10 in [3, 7, 9]:
            y = str(y[:i]) + str(x // 10) + str(y[i+1:])
            i += 1
        x = x // 10
    return y[::-1] if shift > len(str(y)) else y
