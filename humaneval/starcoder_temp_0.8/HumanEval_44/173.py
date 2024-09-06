

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
    if not 2 <= base <= 10:
        raise ValueError("base must be between 2 and 10")

    if base == 10:
        return str(x)

    digits = []
    while x!= 0:
        digits.append(int(x % base))
        x = x // base
    digits.reverse()

    return "".join(str(d) for d in digits)
