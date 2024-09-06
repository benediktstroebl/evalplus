
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    def get_digit(digit_index):
        return str(x // 10 ** digit_index % 10)
    num_digits = len(str(x))
    return ''.join(get_digit((digit_index + shift) % num_digits)
                   for digit_index in range(num_digits))
