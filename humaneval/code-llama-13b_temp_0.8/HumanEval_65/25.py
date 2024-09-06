
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Split the digits into a list.
    digits = list(str(x))
    # Reverse the list if the shift is larger than the number of digits.
    if shift > len(digits):
        digits.reverse()
        return ''.join(digits)
    # Otherwise, shift the digits by slicing the list.
    else:
        return ''.join(digits[shift:] + digits[:shift])

