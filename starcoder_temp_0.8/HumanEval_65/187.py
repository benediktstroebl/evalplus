
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # your code here
    if shift == 0:
        return str(x)
    else:
        string = str(x)
        return string[-shift:] + string[0:len(string)-shift]
