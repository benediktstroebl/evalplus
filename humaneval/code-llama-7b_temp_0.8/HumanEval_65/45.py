
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift == 0:
        return str(x)
    if x < 10:
        return str(x)
    shift_copy = shift
    x_copy = x
    digits = []
    while x_copy > 9:
        digits.append(x_copy % 10)
        x_copy = x_copy // 10
    digits.append(x_copy)
    if shift_copy >= len(digits):
        shift_copy = shift_copy - len(digits)
        return ''.join(map(str, reversed(digits)))
    return ''.join(map(str, reversed(digits[:shift_copy])) + digits[shift_copy:] + 
                   map(str, reversed(digits[:shift_copy])))
