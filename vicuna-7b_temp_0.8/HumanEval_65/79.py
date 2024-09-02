
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    n = len(str(x))
    result = ""
    while n > 0:
        # reverse the digits
        result = "0" + str(int(result[::-1])[::-1])[::-1]
        if n % shift == 0:
            # if shift is less than the number of digits
            # shift the digits to the left
            result = "0" + result
            n -= shift
            shift = shift - 1
        n //= shift
        x = int(x / shift)
        shift = shift - 1
    return result
