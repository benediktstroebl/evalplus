
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    result = []
    original_length = len(str(x))
    digits = [int(i) for i in str(x)]
    for i in range(original_length):
        result.append(digits[i])
    if shift > original_length:
        for i in range(original_length, shift):
            result.append(digits[i % original_length])
    else:
        for i in range(shift):
            result.append(digits[i % original_length])
    return ''.join(map(str, result))
