
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Returning x if shift is 0
    if shift == 0:
        return str(x)
    if x == 0:
        return '0'
    # storing the digits of x
    digits = []
    while x != 0:
        digits.append(x % 10)
        x = x // 10
    # reversing the digits
    digits.reverse()
    # computing the shift
    shift = shift % len(digits)
    if shift > 0:
        for i in range(shift):
            digits.append(digits.pop(0))
    # converting digits back to a string
    return ''.join(map(str, digits))
