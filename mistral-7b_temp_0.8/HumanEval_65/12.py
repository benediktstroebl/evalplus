
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    d = []
    s = str(x)
    for i in s:
        d.append(i)
    res = ""
    while True:
        res = res + d.pop()
        if len(d) == 0:
            return res
        elif shift == 0:
            return res[::-1]
        else:
            if len(d) < shift:
                return res[::-1]
            else:
                shift = shift - 1
    return res
