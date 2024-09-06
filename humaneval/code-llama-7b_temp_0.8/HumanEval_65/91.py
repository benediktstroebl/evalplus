
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert x to a string.
    x_str = str(x)
    # Remove the "-" from x_str if x is negative.
    if x < 0:
        x_str = x_str.replace("-", "")
    # If shift is negative, do the same to shift
    if shift < 0:
        shift = shift * -1
    # If shift is greater than the length of x_str, return digits reversed
    if shift >= len(x_str):
        return x_str[::-1]
    else:
        # Remove the last digits of x_str equal to shift
        x_str = x_str[:-shift]
        # Concatenate the last digits of x_str and the first digits of x_str
        x_str = x_str[-shift:] + x_str[:-shift]
        return x_str
