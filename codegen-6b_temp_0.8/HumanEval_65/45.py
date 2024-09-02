
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x %= MODULUS
    new_x = (x - shift) % MODULUS
    if 0 <= new_x < MODULUS:
        return str(new_x)
    elif new_x < 0:
        return str(MODULUS - new_x)
    else:
        return str(new_x + MODULUS)

