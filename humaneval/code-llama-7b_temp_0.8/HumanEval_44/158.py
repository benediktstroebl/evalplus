

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
    return str(x).lstrip('-')[::-1].zfill(16) \
        .replace('0', '00').replace('1', '01').replace('2', '10') \
        .replace('3', '011').replace('4', '110').replace('5', '101') \
        .replace('6', '111').replace('7', '010')[::-1].lstrip('0')
