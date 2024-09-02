

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
    assert base <= 10, "base must be less or equal to 10"
    return int(x) if base == 10 else "".join(
        str(x // base**i % base) for i in range(int(math.log(x, base)), -1, -1)
    )


