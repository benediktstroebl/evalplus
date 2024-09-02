
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
    while x > 0:
        digits.append(x % 10)
        x //= 10
    # print(digits)
    # print(digits[0])
    digits = digits[shift:] + digits[:shift]
    # print(digits)
    if shift == len(digits):
        return ''.join([str(i) for i in digits])
    else:
        return ''.join([str(i) for i in digits])[::-1]





























































































































