

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
    if x < 0:
        raise ValueError("Expecting number greater than 0.")

    if base < 2 or base > 9:
        raise ValueError("Expecting base between 2 and 9.")

    if x == 0:
        return str(0)

    result = []
    while x:
        x, digit = divmod(x, base)
        result.append(str(digit))

    result.reverse()
    return "".join(result)

