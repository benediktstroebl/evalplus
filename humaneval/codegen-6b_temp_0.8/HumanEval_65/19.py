
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # x, shift = map(int, (x, shift))
    # assert 0 <= x < 10 ** 10
    # assert 0 <= shift < 10 ** 10
    #
    # # add 1 to shift to handle negative shift values
    # shift = (shift + 1) % 10 ** 10
    # number_of_digits = len(str(x))
    # return str(x)[(shift + number_of_digits - 1) % number_of_digits] \
    #     if shift >= number_of_digits else \
    #         str(x)[:(number_of_digits - shift - 1) % number_of_digits]

    return str(x)[(shift % len(str(x))) - 1] if shift >= len(str(x)) else str(x)[:shift - 1]

