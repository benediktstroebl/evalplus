

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
    assert base >= 2 and base <= 10, "Invalid base"
    ans = ""
    while x:
        y = x % base
        if y < 10:
            ans = str(y) + ans
        else:
            ans = str(chr(ord("A") + y - 10)) + ans
        x //= base
    return ans
