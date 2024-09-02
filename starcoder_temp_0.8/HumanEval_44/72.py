

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

    def val(i):
        if i >= len(symbols):
            raise ValueError("Unexpected value")
        return symbols.find(i)

    symbols = string.digits + string.ascii_letters
    result = ''
    base = int(base)
    while x > 0:
        x, i = divmod(x, base)
        result = symbols[i] + result
    return result
