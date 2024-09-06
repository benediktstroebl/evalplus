

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
        raise ValueError("Input number cannot be negative")
    elif x == 0:
        return "0"
    
    # assert base >= 2
    # assert 10**int(math.log(base, 10)) >= base
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if base < 10:
        str_num = str(x)
    else:
        str_num = []
        while x > 0:
            str_num.append(digits[x % base])
            x //= base
    
    return "".join(str_num[::-1])

