
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if type(x) != int or type(shift) != int or x < 0 or shift < 0:
        raise ValueError('Both parameters must be nonnegative integers')
    shifted_str = str(x)[shift:] + str(x)[:shift]
    return shifted_str
