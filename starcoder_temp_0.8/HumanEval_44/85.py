

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
    assert type(x) == int, "input is not a number"
    assert type(base) == int and base > 1, "input base must be an integer greater than 1"
    assert x >= 0, "input number is negative"
    b = string.digits + string.ascii_uppercase

    if x == 0:
        return "0"

    res = []
    while x!= 0:
        res.append(b[x % base])
        x //= base

    return "".join(res[::-1])
