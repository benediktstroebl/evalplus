
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    n = int(len(str(x)))
    shift = int(shift)
    result = ""
    for i in range(n):
        if i < shift:
            result = "0" + result
        result = str(x % 10) + result
        x = x // 10
    return result
