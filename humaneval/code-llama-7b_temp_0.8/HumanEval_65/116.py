
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # reverse the string version of the integer
    # use reversed to reverse a string and then join to create a string
    x_string = str(x)
    x_string_reversed = ''.join(reversed(x_string))

    # reverse the integer version of the integer
    # convert to a string
    x_reversed_string = str(int(x_string_reversed))

    # use slice notation to reverse the string version of x
    # the x[:0] is the string representation of 0
    # the shift specifies how many characters we want to skip
    # the x[shift:] is the remaining characters
    # and then we join them together with '' to make a string
    x_reversed_shifted = ''.join(x_reversed_string[shift:][:0])
    return x_reversed_shifted

