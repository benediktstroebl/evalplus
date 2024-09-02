

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
    if base < 2 or base > 10:
        raise ValueError("Base number is out of range. Please use less than 10 base numbers.")
    result = ''
    while x > 0:
        temp = x % base
        if temp < 10:
            result = str(temp) + result
        else:
            if base == 2:
                result = str(10 + temp) + result
            elif base == 3:
                result = str(20 + temp) + result
            elif base == 4:
                result = str(30 + temp) + result
            elif base == 5:
                result = str(40 + temp) + result
            elif base == 6:
                result = str(50 + temp) + result
            elif base == 7:
                result = str(60 + temp) + result
            elif base == 8:
                result = str(70 + temp) + result
            elif base == 9:
                result = str(80 + temp) + result
    
