
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = []
    x = str(x)
    while x:
        digits.append(int(x[-1]))
        x = x[:-1]
    print(digits)
    # 12345
    # 2345
    # 345
    # 45
    # 5
    # 5
    # 5
    # 5
    # 5
    # []
    result = []
    while len(digits) > shift:
        result.append(digits.pop())
    if shift > len(digits):
        result.extend(digits)
        return "".join(reversed(result))
    else:
        result.extend(digits[:shift])
        return "".join(result)
    # result = []
    # while len(digits) > shift:
    #     result.append(digits.pop())
    # if shift > len(digits):
    #     result.extend(digits)
    #     result.reverse()
    #     return "
