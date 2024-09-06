
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # use string representation of x to get the digits
    x = str(x)
    num_digits = len(x)
    if shift == num_digits:
        return x[::-1]
    elif shift >= num_digits:
        # shift >= num_digits
        # check if shift is even
        if shift % 2 == 0:
            # shift is even
            return x[shift // 2:] + x[:shift // 2]
        else:
            # shift is odd
            return x[(shift - 1) // 2] + x[:(shift - 1) // 2]
    else:
        # shift < num_digits
        return x[shift:] + x[:shift]
