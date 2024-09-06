
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert x to a string and make it a list
    x = str(x)
    x = list(x)

    if shift > len(x):
        shift = shift % len(x)
        x = x[::-1]
    else:
        x = x[len(x) - shift:] + x[:len(x) - shift]

    return "".join(x)
