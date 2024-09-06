
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    list_x = [int(i) for i in str(x)]
    length = len(list_x)
    if shift == 0:
        return "".join(list_x)
    elif shift < length:
        return "".join([list_x[i + shift] for i in range(length)])
    else:
        return "".join([list_x[i - (shift - length)] for i in range(length)])
