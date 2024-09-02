

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

    digits = [str(x) for x in range(10)]
    quotient, remainder = divmod(x, base)
    result = digits[remainder] + change_base(quotient, base) if quotient else digits[remainder]
    return result

