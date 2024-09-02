

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
    if base < 2 or base > 10:
        raise ValueError("Base is not in range!")
    elif x < 0 or x > 10:
        raise ValueError("Number is out of range!")

    # convert to base 10
    x = int(x)

    # convert to base
    res = ""
    while x:
        x, r = divmod(x, base)
        res = str(r) + res
    return res

