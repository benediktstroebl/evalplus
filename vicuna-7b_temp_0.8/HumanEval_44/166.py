

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
    # convert x and y from base 10 to base 2
    x_2 = str(x)
    x_2 = x_2.zfill(2)
    
    y_10 = str(base)
    y_10 = '0'* (10 - len(y_10)) + y_10
    
    # convert x from base 2 to base 10
    x_10 = x_2[2:] * (10**len(x_2) - 1)
    
    return y_10[len(x_10):] + x_10[:len(x_10)]
