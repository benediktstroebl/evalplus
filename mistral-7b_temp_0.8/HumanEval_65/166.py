
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    import math
    digits = list(str(x))
    n_digits = len(digits)
    shift %= n_digits
    if shift == 0:
        return ''.join(digits)
    if shift == n_digits:
        return ''.join(reversed(digits))
    # print(shift)
    result = []
    for i in range(n_digits):
        n = (i + shift) % n_digits
        result.append(digits[n])
    return ''.join(result)

