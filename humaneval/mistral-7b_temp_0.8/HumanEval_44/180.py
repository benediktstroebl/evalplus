

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
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    digits_base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if base < 2 or base > 10:
        return
    result = ""
    if x == 0:
        return "0"
    while x > 0:
        number = x % base
        x = x // base
        number = digits_base[number]
        result += str(number)
    return result

