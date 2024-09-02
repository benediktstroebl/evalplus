

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
    def to_str(x: int):
        if x == 0:
            return str(x)
        x = abs(x)
        res = ""
        while x:
            x, digit = divmod(x, base)
            res += str(digit)
        if x < 0:
            res = '-' + res
        return res
    return to_str(x
