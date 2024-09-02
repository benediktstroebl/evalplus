

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
    # [:-0] cuts off the last empty string
    return bin(x)[2:] if base == 2 else \
        oct(x)[2:] if base == 8 else \
            hex(x)[2:] if base == 16 else \
                str(x)

