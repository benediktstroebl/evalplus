
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    def circular_shift_helper(num, digit_count, shift):
        digit_count = digit_count - shift
        if shift > digit_count:
            shift = shift % digit_count
        if shift > 0:
            return circular_shift_helper(num, digit_count, shift - 1)
        return num

    return str(circular_shift_helper(x, len(x), shift))
