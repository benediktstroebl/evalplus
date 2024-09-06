

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
    result = []
    while x >= base:
        quotient, remainder = divmod(x, base)
        result.append(remainder)
        x = quotient

    result.append(x)

    return ''.join(str(x) for x in result[::-1])


