
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x = str(x)
    # print(x)
    # print(len(x))
    shift = shift % len(x)
    # print(shift)
    result = x[len(x) - shift:] + x[: len(x) - shift]
    # print(result)
    return result

