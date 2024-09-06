
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = map(str, x)
    reversed_digits = digits[::-1]
    new_digits = list(reversed_digits)
    for i in range(shift):
        new_digits.remove(new_digits[0])
        new_digits.append(new_digits[-1])
    return ''.join(new_digits)