

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
        return "Invalid base!"
    new_number = []
    while x:
        new_number.append(int(x % base))
        x = x // base
    new_number.reverse()
    return "".join(str(i) for i in new_number)
