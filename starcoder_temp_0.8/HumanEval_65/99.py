
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert to a string
    x = str(x)
    # Reverse the digits of x
    x = x[::-1]
    # Calculate the number of digits
    digits = len(x)
    # Calculate the amount to shift by, then shift
    shift = shift % digits
    shifted = x[shift:] + x[:shift]
    # Return shifted
    return shifted
