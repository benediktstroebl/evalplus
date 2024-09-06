

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
    # check whether the number is valid
    assert base > 1 and base <= 10, 'base should be less than 10 and greater than 1'

    # get the absolute value of input x
    x = abs(x)

    # initialize the result
    result = ''

    # add the digits to the beginning of the string
    while x > 0:
        result = str(x % base) + result
        x = x // base

    return result
