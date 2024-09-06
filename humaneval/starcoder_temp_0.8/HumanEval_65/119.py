
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    num_digits = len(s)
    digits = [int(d) for d in s]
    for i in range(shift):
        digits.append(digits[0])
        digits = digits[1:]
    if shift >= num_digits:
        return "".join([str(d) for d in digits])
    return "".join([str(d) for d in digits[-shift:]])

