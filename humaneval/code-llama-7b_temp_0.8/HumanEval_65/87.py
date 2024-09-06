
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Base case
    if x == 0:
        return "0"
    # Recursive case
    else:
        # Check if x has digits left to shift
        if x % 10 ** (len(str(x)) - 1) != 0:
            return str(x % 10 ** (len(str(x)) - 1)) + circular_shift(x // 10, shift)
        # Return reversed digits if no digits left to shift
        else:
            return str(x % 10) + circular_shift(x // 10, shift)

