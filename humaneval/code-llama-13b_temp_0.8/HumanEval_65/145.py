
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
    for i in range(len(str(x))):
        result.append(str((x//(10**i))%10))
    if shift >= len(result):
        return ''.join(result[::-1])
    for i in range(len(result)):
        if i < len(result)-shift:
            result[i], result[i+shift] = result[i+shift], result[i]
    return ''.join(result)

