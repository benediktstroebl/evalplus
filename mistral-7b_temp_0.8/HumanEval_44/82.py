

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
    print("change_base: x, base")
    if type(x) != int:
        raise ValueError("x is not int")

    if type(base) != int:
        raise ValueError("base is not int")

    if base < 2 or base > 10:
        raise ValueError("base is not a valid base")

    result = ""
    while x > 0:
        result = str(x % base) + result
        x = int(x / base)
    return result

