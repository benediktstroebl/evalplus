

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
    power = 0
    power_p = 1
    result = []
    while x != 0:
        digit = x % base
        if digit > 9:
            result.append(chr(ord('A') + digit - 10))
        else:
            result.append(str(digit))
        x = (x - digit) // base
        power += power_p * digit
        power_p *= 10
    result.reverse()
    result.append(str(power))
    return ''.join(result)
