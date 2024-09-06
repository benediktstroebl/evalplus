
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    a = list(str(abs(x)))
    result = []
    for i, c in enumerate(a):
        result.insert(i + shift, c)
    a = ''.join(result)
    if x >= 0:
        return a
    else:
        return a[1:] + a[0]

