

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
    if x < 0:
        return change_base(-x,base)
    if x < 10:
        return str(x)
    if x < 100:
        return change_base(x//10, base) + str(x%10)
    if x < 1000:
        return change_base(x//100, base) + '0' + change_base(x%100, base)
    return change_base(x//1000, base) + '00' + change_base(x%1000, base)
