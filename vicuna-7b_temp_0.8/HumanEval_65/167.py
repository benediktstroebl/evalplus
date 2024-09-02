
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # split x into its individual digits
    x = [int(d) for d in x]
    # reverse the digits if shift is greater than the number of digits
    if shift > len(str(x[0])):
        x = [reversed(d) for d in x]
    # concatenate the reversed digits to get the circular shift
    return ''.join(x)