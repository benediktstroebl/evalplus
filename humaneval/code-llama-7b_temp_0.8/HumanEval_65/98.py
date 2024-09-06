
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert to string
    x = str(x)

    # If shift is greater than the length of x, return x reversed
    if shift >= len(x):
        return x[::-1]

    # Get the remainder of shift / len(x)
    # To determine how many times to shift the digits to the right
    remainder = shift % len(x)

    # If remainder is zero, no need to shift
    if remainder == 0:
        return x

    # Pad remainder to the length of x so that it can be reversed
    remainder = remainder * "0" + str(remainder)

    # Reverse the remainder
    remainder = remainder[::-1]

    # Convert the remainder to an integer
    remainder = int(remainder)

    # Shift the digits to the right by remainder
    x = x[-remainder:] + x[:-remainder]

    return x

