

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
    # create empty string
    result = ''
    # check if x is positive
    if x < 0:
        return 'ERROR: negative input!'

    # while number > 0 do
    while x > 0:
        # get remainder
        remainder = x % base
        # convert remainder to string
        result = str(remainder) + result
        # remove last digit from x
        x //= base
    return result

