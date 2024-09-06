

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
    if not base > 10:
        print("Invalid base number")
    else:
        res = ""
        for i in range(0, base):
            if x < base:
                res += str(x)
            x = x % base
        return res
