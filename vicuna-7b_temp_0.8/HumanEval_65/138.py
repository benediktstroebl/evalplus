
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    result = ""
    while x > 0:
        if x % 10 > 0:
            result = "0" + result
        result = "0" + str(x // 10) + result[1:]
        x //= 10
    return result
