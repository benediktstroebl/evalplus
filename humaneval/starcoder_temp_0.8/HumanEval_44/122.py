

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
    assert 2 <= base <= 10, "base must be between 2 and 10"

    digits = "0123456789ABCDEF"
    stack = []
    while x > 0:
        stack.append(digits[x % base])
        x = x // base
    return "".join(stack[::-1])
