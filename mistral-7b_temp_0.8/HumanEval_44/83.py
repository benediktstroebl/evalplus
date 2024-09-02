

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
    # if base is 0, return ''
    if base == 0:
        return ''
    # if x is 0, return 0
    elif x == 0:
        return '0'
    # if x is negative, convert to positive
    else:
        x = abs(x)
        # store the string representation of x in str_x
        str_x = ''
        # while x is greater than 0
        while x > 0:
            # use modulo to get the remainder
            remainder = x % base
            # append the remainder to the str_x
            str_x = str(remainder) + str_x
            # divide x by base to get the quotient
            x = x // base
    # convert str_x to int
    str_x = int(str_x)
    # return str_x
    return str_x
