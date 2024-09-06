

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
    # precondition
    assert base > 0 and base < 10, "base must be greater than 0 and less than 10"

    if x == 0:
        return '0'
    digits = []
    while x > 0:
        remainder = x % base
        x = x // base
        digits.insert(0, str(remainder))

    return ''.join(digits)

