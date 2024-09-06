
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = list(str(x))
    n = len(digits)
    n_shifts = n - shift
    if n_shifts < 0:
        digits.reverse()
        digits.extend(["0"] * abs(n_shifts))
    else:
        digits.extend(["0"] * n_shifts)
    return "".join(digits
