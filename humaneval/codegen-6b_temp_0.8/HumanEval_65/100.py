
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # don't try this at home!
    # This is an example of a tester function call.
    # The first argument is the function name,
    # and the rest of the args are what the function
    # is called with.
    # This is just an example; replace it with your code.
    return str(x)[-shift:] + str(x)[:-shift]


