

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

    if x == 0:
        return '0'
    if base <= 10:
        return change_base_internal(x, base)
    result = change_base_internal(x, base)
    power = 0
    while result[0] == '0' and len(result) > 1:
        result = result[1:]
        power += 1
    return change_base_internal(int(result), base) + '10' * power

