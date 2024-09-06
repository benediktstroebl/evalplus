
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift >= len(str(x)) % shift:
        return str(x)
    else:
        return str(int(x) * (10**(shift-len(str(x))%shift)) + int(x) % (10**shift))[::-1]
