

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
        raise ValueError("must be a positive integer")

    def iter(x, base):
        # convert x to base
        result = ''
        while x > 0:
            result = str(x % base) + result
            x //= base
        return result

    return iter(x, base)

