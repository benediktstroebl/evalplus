
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
    if shift == 0:
        return str(x)
    # if shift > number of digits
    if x < 10**(shift-1):
        return str(x)[::-1]
    # Recursive case
    else:
        return str(x%10) + circular_shift(x//10, shift-1)
