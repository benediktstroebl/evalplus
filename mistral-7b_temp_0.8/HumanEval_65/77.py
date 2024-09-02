
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
    tmp = x
    for i in range(shift):
        if tmp // 10 > 0:
            result = str(tmp % 10) + result
            tmp = tmp // 10
        else:
            result = "0" + result
    for i in range(len(str(x)) - shift):
        if x // 10 > 0:
            result = str(x % 10) + result
            x = x // 10
        else:
            result = "0" + result
    return result

