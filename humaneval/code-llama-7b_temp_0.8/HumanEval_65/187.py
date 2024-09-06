
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if not isinstance(shift, int):
        return "ERROR"
    if not shift >= 0:
        return "ERROR"
    if not isinstance(x, int):
        return "ERROR"
    if not x >= 0:
        return "ERROR"

    result = ""
    num = str(x)
    for i in range(shift):
        result = num[1:] + num[0]
        num = result

    return result

