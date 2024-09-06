
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Get the number of digits of x
    n = len(str(x))
    # Shift the digits right by shift
    x = int(str(x)[n - shift:] + str(x)[: n - shift])
    # If x has more than n digits, return the digits reversed
    if len(str(x)) > n:
        return str(x)
    # Else return the number of digits of x
    return str(x)
