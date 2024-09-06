
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # handle special case where shift is zero
    if shift == 0:
        return "0"
    # handle special case where x is zero
    if not x:
        return "0"
    # pad x with leading zeros to ensure correct shifting
    x_str = str(x)
    if x_str[-1] < shift:
        x_str += "0" * (shift - len(x_str) % shift)
    # shift the digits to the right and pad with leading zeros
    return "".join([x_str[i:i+shift] for i in range(0, len(x_str), shift)])
