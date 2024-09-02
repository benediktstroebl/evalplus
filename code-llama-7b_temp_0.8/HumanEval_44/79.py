

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
    return str(x).lstrip('-') if x < 0 else '' + \
        str(x).lstrip('-').replace('0', '').rjust(len(str(x)), '0') \
        if x else '0' if x == 0 else ''

