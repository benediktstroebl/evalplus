

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
    # your code
    # base 2 and 10
    base_str = "01"
    if base == 10:
        return str(x)
    if base == 2:
        return bin(x)[2:]

    # base 11+
    num = x
    # negative
    if num < 0:
        is_neg = True
        num = -num
    else:
        is_neg = False
    output_str = ''
    while num > 0:
        output_str = base_str[num % base] + output_str
        num //= base
    if is_neg:
        output_str = '-' + output_str
    return output_str

