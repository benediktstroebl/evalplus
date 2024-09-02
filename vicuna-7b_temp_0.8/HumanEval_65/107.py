
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = [str(d) for d in x]
    while len(digits) > 0:
        n = len(digits[0])
        carry = 0
        for d in digits[1:]:
            n = max(n, int(d))
            d = int(d)
            carry += d / 10
            d = d % 10
        digits[0] = str(sum(digits[1:])) + str(carry)
        digits = digits[1:]
    return ''.join(digits)
