

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
    if base < 2 or base > 10:
        raise ValueError('base must be between 2 and 10')
    return str(x).replace('0', '0').replace('1', '1').replace('2', '2').replace('3', '3').replace('4', '4').replace('5', '5').replace('6', '6').replace('7', '7').replace('8', '8').replace('9', '9')
