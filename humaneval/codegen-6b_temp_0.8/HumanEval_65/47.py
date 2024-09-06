
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if x == 0:
        return None

    # Get the length of the number
    length = len(str(x))

    # Shift the number
    shifted = (x % 10**(length - shift)) // 10**(length - shift - 1)

    # Get the last shift digits
    last = (x // 10**(length - shift - 1)) % 10

    # Add on to the last shift digits
    return str(last) + str(shifted)

