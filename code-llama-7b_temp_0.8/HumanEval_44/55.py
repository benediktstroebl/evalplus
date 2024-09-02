

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

    # declare string representation of the number
    s = ''

    # loop till number is greater than zero
    while x > 0:
        # append the remainder to the string
        s += str(x % base)
        # integer division by base
        x //= base

    return s

