

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
    # your code here
    # each line of code should be indented, please check the indentation.
    result = ''
    while x > 0:
        r = x % base
        x = x // base
        if r >= 10:
            result = chr(r + 87) + result
        else:
            result = str(r) + result
    return result

