

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
    if base > 9:
        return ""
    for i in range(x, 0, 10):
        if x % i == 0:
            y = x // i
            remainder = x % i
            if remainder == 0:
                return f"{y}0"
            else:
                return f"{y}{remainder}1"
    return ""
