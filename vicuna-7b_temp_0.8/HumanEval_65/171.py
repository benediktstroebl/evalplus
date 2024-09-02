
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = map(int, str(x))
    shift_num = 0
    result = ""
    for i in range(shift - len(str(x)), -1, -1):
        result = digits[i] + result
        shift_num += 1
    if shift_num > len(str(x)):
        shift_num = 0
        result = digits[shift_num] + result + digits[shift_num + 1] + digits[shift_num + 2] + digits[shift_num + 3]
    return str(result)
