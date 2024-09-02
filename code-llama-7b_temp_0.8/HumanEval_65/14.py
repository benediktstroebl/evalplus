
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert isinstance(x, int), "The input argument x must be an integer."
    assert x >= 0, "The input argument x must be a non-negative integer."
    assert isinstance(shift, int), "The shift parameter must be an integer."
    assert shift >= 0, "The shift parameter must be a non-negative integer."
    assert shift <= len(str(x)), "The shift parameter must not exceed the number of digits of the input argument x."
    # BEGIN_SOLUTION
    return str(int(str(x)[shift:] + str(x)[:shift]))
    # END_SOLUTION

