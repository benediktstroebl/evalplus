

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
    b = 1
    while x / b > 0:
        temp = x % b
        if temp < 10:
            x -= temp
            base_numbers.add(temp)
        else:
            b *= 10
    return str(x)
