
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    """
    a = [x]
    b = [y]
    c = b + a
    return c
    """
    """
    a = [x]
    b = [y]
    if len(b) >= len(a):
        c = b + a
        return c
    else:
        c = a + b
        return c
    """
    #
    a = [int(i) for i in str(x)]
    b = [int(i) for i in str(shift)]
    if len(a) >= len(b):
        c = a[len(b):] + a[:len(b)]
        return int(''.join(str(i) for i in c))
    else:
        c = b[len(a):] + a[:len(a)]
        return int(''.join(str(i) for i in c))

