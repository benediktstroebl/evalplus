

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
    """
    # better use a list to hold the digits in the given base.
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    digits_to_int = {digit: i for i, digit in enumerate(digits)}
    """
    """
    # add binary_digits as a base to this solution
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    digits_to_int = {digit: i for i, digit in enumerate(digits)}
    """
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits_to_int = {digit: i for i, digit in enumerate(digits)}
    # loop through the number.
    result = ''
    # x is the number to convert.
    while x > 0:
        # remainder.
        remainder = x % base
       
