
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # split x into digits
    digits = [int(d) for d in str(x)]
    # reverse digits if shift is greater than number of digits
    if shift > len(digits):
        reverse_digits = digits[::-1]
    else:
        reverse_digits = digits[len(digits)-shift:] + digits[:len(digits)-shift]
    # reverse, join, and convert back to integer from string
    return int(''.join([str(d) for d in reverse_digits]))

