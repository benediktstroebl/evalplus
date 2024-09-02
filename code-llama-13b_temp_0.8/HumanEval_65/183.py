
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x = str(x)
    # Get the number of digits of x
    num = len(x)
    # If shift is greater than the number of digits, just reverse the digits
    if shift > num:
        x = x[::-1]
    # If not, get the shifted digits
    else:
        # Split x into a list of digits
        x = list(x)
        # Do the circular shift
        x = x[num - shift:] + x[:num - shift]
        # Join the list to create a string
        x = "".join(x)
    return x

