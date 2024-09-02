

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
        sign = '-'
    else:
        sign = ''
    x = abs(x)
    base_num = ''
    while x > 0:
        # Determine remainder of x divided by base, x = remainder + base * remainder of x divided by base
        remainder = x % base
        x = int(x / base)
        # Determine converted digit
        if remainder > 9:
            converted_digit = chr(ord('a') + remainder - 10)
        else:
            converted_digit = str(remainder)
        # Prepend digit to converted number
        base_num = converted_digit + base_num
    return sign + base_num

