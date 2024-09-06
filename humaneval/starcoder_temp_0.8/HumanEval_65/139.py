
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    shift_str = str(shift)
    digits = [int(c) for c in str(x)]

    if shift < 0:
        raise ValueError("shift must be positive")
    elif shift == 0:
        return str(x)
    else:
        shift_digits = [digits[-1 - i] for i in range(shift)]
        rest_digits = [digits[-1 - i] for i in range(shift, len(digits))]

        shifted = rest_digits + shift_digits
        return "".join(str(d) for d in shifted)

