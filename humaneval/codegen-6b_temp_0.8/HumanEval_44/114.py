

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x < 0:
        raise ValueError("Negative numbers cannot be converted to base.")
    if base < 2 or base > 36:
        raise ValueError("Base can only be 2 to 36.")
    if x == 0:
        return "0"

    x = list(str(x))
    x.reverse()
    length = len(x)
    factor = 1
    result = []
    while length > 0:
        flag = (base ** factor)
        if length > factor:
            result.append(x[factor])
            length -= factor
        else:
            z = x[length-1]
            while flag > 1:
                try:
                    z = list(str(int(z) + 1))[0]
                    flag -= 1
                except IndexError:
                    z = '9'
            result.append(z)
            length -= 1
        factor += 1
    result.reverse()
    return ''.join(result)
