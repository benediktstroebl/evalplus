
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = [str(d) for d in x]
    result = ''.join(digits)
    for i in range(shift, len(result)):
        result = result[:i] + str(ord(result[i])-ord('0')+shift) + result[i+1:]
    return result[::-1] if shift > len(result) else result
