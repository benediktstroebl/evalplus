
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    sign = 1 if x < 0 else 0
    mag = abs(x)
    y = str(int(mag * 10 + sign))
    return "".join(map(str, map(lambda x: y[x.index(y.index(str(x)))] if x in y else y[x.index(y.index(str(y[y.index(str(y[y.index(str(y[y.index(str(y))]))]))]))], y)))[::-1]) if shift <= len(y) else y[::-1]
