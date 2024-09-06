
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # BEGIN PROBLEM 3
    if x < 0:
        return circular_shift(-x, shift)
    return str(int(x * 10**(shift % len(str(x))) % 10**len(str(x))) * int(10**(len(str(x)) - shift % len(str(x)))))
    # END PROBLEM 3

