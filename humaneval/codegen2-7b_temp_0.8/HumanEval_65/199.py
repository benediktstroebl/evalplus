
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = []
    for i in str(x):
        if i!= "0":
            digits.append(i)
    if len(digits) < shift:
        shift = shift - len(digits)
        digits = digits[-shift:] + digits[:-shift]
    return "".join(digits
