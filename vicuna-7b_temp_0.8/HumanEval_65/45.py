
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    shift = int(shift)
    if shift > len(str(x)) - len("0"):
        shift = len("0") - 1 - shift
    sign = "+" if x >= 0 else "-"
    head, tail = "0", str(x)
    while len(tail) >= shift:
        head = head[:-1]
        x = x // 10
        tail = str(x)
    return sign + head + str(int(tail) % 10)
