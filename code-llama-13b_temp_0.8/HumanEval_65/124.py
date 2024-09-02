
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
    x = list(str(x))
    x.reverse()
    x = int(''.join(x))
    if shift >= len(str(x)):
        shift = len(str(x)) - shift
    x = list(str(x))
    for i in range(0, shift):
        x.insert(0, x[-1])
        x.pop()
    return ''.join(x)
