
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # write x in binary
    x_binary = str(x)
    # reverse the string
    x_binary = x_binary[::-1]
    # shift the digits
    for i, digit in enumerate(x_binary):
        # if shift is 0, return original number
        if shift == 0:
            return x_binary
        # shift the digits to the right, zero-padding with leading zeroes
        shift_digits = (digit << shift) & (0xffffffff << (32 - shift * 2))
        x_binary = x_binary[:i] + (shift_digits >> (32 - len(x_binary) * 8)) + x_binary[i+1:]
    # return reversed digits if shift > number of digits
    if shift > len(x_binary):
        return x_binary[::-1]
    return x_binary
