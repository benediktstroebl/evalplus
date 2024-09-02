
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # A list of the digits in x
    digits = []
    # make digits
    while x > 0:
        digits.append(x % 10)
        x = x // 10
    # reverse if shift > number of digits
    if shift > len(digits):
        return "".join(map(str, reversed(digits)))
    # circular shift
    for i in range(shift):
        digits.append(digits.pop(0))
    return "".join(map(str, digits))

