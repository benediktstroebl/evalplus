

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
    if base == 10:
        return str(x)
    else:
        return str(x).replace('0', 'O').replace('1', 'I').replace('2', 'Z').replace('3', 'S').replace('4', 'T').replace('5', 'H').replace('6', 'B').replace('7', 'N')
    
    
