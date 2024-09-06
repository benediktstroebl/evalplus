

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
    assert 1 <= base <= 10
    """
    if x == 0:
        return "0"
    digits = ""
    while x > 0:
        x, remainder = divmod(x, base)
        digits = str(remainder) + digits
    return digits
    """
    if x == 0:
        return "0"
    digits = []
    while x > 0:
        x, remainder = divmod(x, base)
        digits.append(str(remainder))
    return "".join(digits[::-1])

