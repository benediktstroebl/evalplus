
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # convert the number to string
    x_string = str(x)
    # if the length of the number is less than shift
    if len(x_string) < shift:
        # reverse the number
        return x_string[::-1]
    # if the length of the number is greater than or equal to shift
    else:
        # shift the number right by shift digits
        return x_string[shift:] + x_string[:shift]
