
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    num_digits = 0
    while x > 0:
        num_digits += 1
        x = x // 10
    shift = shift % num_digits
    if shift == 0:
        return str(x)
    l = [int(i) for i in str(x)]
    return "".join(str(i) for i in l[-shift:] + l[:-shift])

