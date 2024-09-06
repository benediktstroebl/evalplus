
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift <= 0:
        return "".join(reversed(str(x)))

    def circular_shift_helper(x, shift):
        if shift == 0:
            return x

        return circular_shift_helper(10 * (x % 10) + x // 10, shift - 1)

    return str(circular_shift_helper(x, shift))



