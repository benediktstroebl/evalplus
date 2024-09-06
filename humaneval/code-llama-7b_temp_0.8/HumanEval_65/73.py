
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
    if x == 0:
        return str(x)

    digits = []
    while x != 0:
        digits.append(x % 10)
        x //= 10

    if len(digits) < shift:
        for _ in range(shift - len(digits)):
            digits.append(digits[0])
            del digits[0]

    elif len(digits) > shift:
        for _ in range(shift):
            digits.append(digits[0])
            del digits[0]

    return ''.join(str(digit) for digit in digits)
