

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
    assert 10 > base >= 2, "base has to be lower than 10"
    result = ""
    number = x
    while number:
        result += str(number % base)
        number = number // base
    return result[::-1]

