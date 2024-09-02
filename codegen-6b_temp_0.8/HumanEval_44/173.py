

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
    d = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    if base > 10 or base < 2:
        return ""
    else:
        if x == 0:
            return "0"
        else:
            digits = []
            while x > 0:
                digits.insert(0, x % base)
                x = x // base
            return "".join([d[dnum] for dnum in digits])
