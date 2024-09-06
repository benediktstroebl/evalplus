
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    "*** YOUR CODE HERE ***"
    res = ''
    if shift > 0:
        res = str(x)[shift:] + str(x)[:shift]
    else:
        res = str(x)[abs(shift) - 1::-1]
    return res

