
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the number to a string
    # pylint: disable=redefined-outer-name
    x_str = str(x)
    # Get the length of the string
    length = len(x_str)
    # Get the shifted string
    shifted = x_str[::-1]
    # Get the length of the shifted string
    shifted_length = len(shifted)
    # Pad the left side of the shifted string with zeroes
    shifted = "0" * (shifted_length - length) + shifted
    # Convert the string back to an integer
    # pylint: enable=redefined-outer-name
    return int(shifted)
