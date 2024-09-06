
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift >= len(str(x)) or shift < 0:
        return str(x)[:-shift] + str(x)[-shift:]
    else:
        result = str(x)
        for i in range(shift):
            result = result[:-1] + result[1:]
        return result