
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # convert to a string so that we can rotate each digit
    x = str(x)
    length = len(x)
    remainder = shift % length

    # if shift is greater than the number of digits
    if remainder == 0:
        # don't do anything
        return x

    # calculate the new start point
    start = (length - remainder) + 1
    # need to use slice syntax due to the nature of strings
    new_digits = x[start:] + x[:start]
    return new_digits

