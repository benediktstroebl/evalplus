

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
    
    """
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    """
    digits = "0123456789"
    """
    result = ""
    if x < base:
        return digits[x]
    while x != 0:
        x, i = divmod(x, base)
        result = digits[i] + result
    return result

