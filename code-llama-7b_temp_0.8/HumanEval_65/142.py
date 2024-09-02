
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    a = str(x)
    b = []
    if len(a) <= shift:
        return a[::-1]
    for i in range(len(a)):
        b.append(a[i+shift])
    return "".join(b)

