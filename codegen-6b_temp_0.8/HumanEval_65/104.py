
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # if shift > number of digits, reverse result
    if shift > len(str(x)):
        print((len(str(x))))
        shift = shift % len(str(x))

    # reverse the string x
    x = str(x)[::-1]

    # circular shift the digits of the integer x
    return ''.join([x[i] for i in range(len(x)-shift, len(x))]) + ''.join([x[i] for i in range(0, len(x)-shift)])


