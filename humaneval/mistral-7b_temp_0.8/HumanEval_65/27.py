
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    # make a copy of the list of digits
    digits = [int(x) for x in str(x)]
    # circular shift the digits
    for i in range(shift):
        # print(digits)
        digit_to_remove = digits.pop()
        digit_to_insert = digits.insert(0, digit_to_remove)
    # create a list of strings
    digits_string = [str(x) for x in digits]
    # convert to string
    digits_string = "".join(digits_string)
    return digits_string
