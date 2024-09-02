
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    result = "0" * len(str(x))
    carry = 0
    for i in range(len(str(x))):
        digit = str(x)[i]
        if i < len(str(x)) - 1 and digit == "0":
            digit = 0
        if carry == 1:
            digit += 1
            carry = 0
        result += digit
        if i % 2 == 1:
            carry = 1
            result += "0"
    return result[:]
