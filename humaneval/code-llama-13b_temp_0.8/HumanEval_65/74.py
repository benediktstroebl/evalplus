
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

    for _ in range(len(str(x))):
        result.append(x % 10)
        x = x // 10

    for i in range(len(result)):
        if i >= shift:
            break
        else:
            result[i], result[-i-1] = result[-i-1], result[i]

    return "".join(map(str, result))

