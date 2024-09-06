
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    result = ""
    # work with x as a string
    x = str(x)
    # if shift is greater than length of x, reverse x
    if shift >= len(x):
        return x[::-1]
    # otherwise, shift the digits over by shift
    for i in range(shift):
        result += x[len(x)-1]
        x = x[:len(x)-1]
    result += x
    return result

