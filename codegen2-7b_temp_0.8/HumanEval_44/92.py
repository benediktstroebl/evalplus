

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
    if base < 1 or base > 10:
        raise ValueError("invalid base")
    if x < 0:
        sign = "-"
        x = -x
    else:
        sign = ""
    digits = [int(i) for i in str(x)]
    return sign + "".join([base ** i for i in digits])

