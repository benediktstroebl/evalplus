
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x_copy = x
    x_string = str(x)
    rev = x_string[::-1]
    if shift > len(str(x)):
        return rev
    else:
        for _ in range(shift):
            x_copy = x_copy // 10
        return str(x_copy) + rev[:-shift]

