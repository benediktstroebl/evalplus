
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # look out for digits of x
    digits = []
    while x:
        digits.append(x % 10)
        x //= 10
    if shift <= len(digits):
        # shift the digits right by shift
        return int(''.join([str(i) for i in digits[shift:]]+[str(i) for i in digits[:shift]]))
    else:
        return int(''.join([str(i) for i in digits[::-1]]))

