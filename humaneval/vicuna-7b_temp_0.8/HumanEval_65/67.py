
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert x to a string and shift the digits to the right
    x = str(x)
    i = len(x) - shift
    while i >= 0:
        x = x[:i] + str(int(x) % (10 ** (len(x) - i - 1)))
        i -= 1
    return x
