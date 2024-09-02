
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # handle special case of shift = 0
    if shift == 0:
        return str(x)
    # handle special case of shift = 1
    if shift == 1:
        return str(x)[::-1]
    # handle shift as an integer
    if isinstance(shift, int):
        result = []
        for i in range(len(str(x))):
            result.append(x % 10)
            x = x // 10
        return ''.join(reversed(result))
    # handle shift as a string
    if isinstance(shift, str):
        shift = int(shift, 2)
        # handle shift as a negative number
        if shift < 0:
            shift = -shift
        # handle special case of shift = 10
        if shift == 10:
            shift = 0
        # handle shift as a positive number
        if shift >= 0:
            return str(x)[:-shift]
    # handle shift as a string
    if isinstance(shift, str):
        shift = int(shift, 2)
        # handle shift as a negative number
        if shift < 0:
            shift = -shift
        # handle special case of shift = 10
        if shift == 10:
            shift = 0
        # handle shift as a positive number
        if shift >= 0:
            return str(x)[::-shift]
    # handle invalid shift value
    raise ValueError("Invalid shift value")
