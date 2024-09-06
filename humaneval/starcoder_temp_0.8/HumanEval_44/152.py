

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
    # initialize list
    digits = []
    # check input
    assert(x>=0 and base>0 and base <10)
    # convert
    while x > 0:
        digits.append(x%base)
        x = x//base
    # convert list to string
    digits.reverse()
    return ''.join([str(digit) for digit in digits])
