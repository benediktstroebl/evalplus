
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # check if shift is greater than number of digits
    if shift > len(str(x)):
        # if shift is greater than number of digits, reverse the number and return
        return str(x)[::-1]
    # else get the digits of the number, list them, shift them right by shift, and reverse them
    return str(x)[shift:] + str(x)[:shift]
