
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    number_of_digits = len(str(x))
    if shift > number_of_digits:
        shift = shift % number_of_digits
    if shift == 0:
        return str(x)
    else:
        #split x into a list of digits
        digits = [int(d) for d in str(x)]
        #rotates the digits list
        digits[shift:] = digits[:shift]
        #rebuild the number from the list
        shifted_digits = [str(d) for d in digits]
        return "".join(shifted_digits)
