
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if x < 10:
        return str(x)

    if x < 100:
        if x % 10 == shift:
            return str(x)
        else:
            return str(x % 10) + str(x // 10)

    if x < 1000:
        if x % 10 == shift:
            return str(x)
        elif x % 100 == shift:
            return str(x // 10) + str(x % 10)
        else:
            return str(x % 10) + str(x // 10)

    if x < 10000:
        if x % 10 == shift:
            return str(x)
        elif x % 100 == shift:
            return str(x // 10) + str(x % 10)
        elif x % 1000 == shift:
            return str(x // 100) + str(x % 100)
        else:
            return str(x % 10) + str(x // 10)

