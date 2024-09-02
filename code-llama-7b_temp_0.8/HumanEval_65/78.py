
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    if x == 0:
        return "0"
    if x < 0:
        return "-" + circular_shift(-x, shift)

    rev_digits = []
    digits = str(x)
    digits_reversed = digits[::-1]
    if shift > len(digits):
        return "".join(digits_reversed)

    for digit in digits:
        rev_digits.append(digits_reversed[shift - 1])
        shift -= 1
        if shift < 0:
            break
    return "".join(rev_digits)

