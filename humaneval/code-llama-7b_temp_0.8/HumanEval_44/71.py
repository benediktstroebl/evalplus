

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
    def change_single_char(x, base):
        """Change single character to new base.
        >>> change_single_char(1, 2)
        '1'
        >>> change_single_char(1, 3)
        '1'
        >>> change_single_char(2, 3)
        '2'
        """
        if base == 10:
            return str(x)
        else:
            return str(chr(ord('0')+x))
    result = []
    while x:
        result.append(change_single_char(x%base, base))
        x = x // base
    return ''.join(result[::-1])

