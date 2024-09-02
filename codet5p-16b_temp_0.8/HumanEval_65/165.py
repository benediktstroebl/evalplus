
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    digit = 0
    res = ""
    while digit < len(x):
        res += str(x[digit])
        digit += 1
    res = res[:-shift] + res[-shift:]
    return res

