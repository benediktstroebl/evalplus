
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    str_x = str(x)
    if shift > len(str_x):
        return "".join(reversed(str_x))

    str_x = str_x * 2
    i, j = 0, 0
    while i < shift:
        i += 1
        j += 1
        if j == len(str_x):
            j = 0
    return str_x[j : j + len(str_x) // 2]

