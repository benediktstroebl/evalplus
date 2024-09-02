
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Find the number of digits in x
    n = len(str(x))
    # Ensure that shift is no more than n
    shift = shift % n
    # Construct the result as a string
    res = str(x)[-shift:] + str(x)[:-shift]
    # Return the result
    return res
