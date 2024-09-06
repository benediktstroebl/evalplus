

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
    # input is integer
    assert isinstance(x, int), "input number must be an integer"
    assert isinstance(base, int), "base must be an integer"
    # base is less than 10
    assert base < 10, "base numbers are less than 10"
    # test if x is positive
    if x >= 0:
        pass
    else:
        x = -x
    # initialize result
    result = ""
    # initialize power
    p = 1
    # convert x to string
    string_x = str(x)
    # calculate the remainder of x/base
    while p <= len(string_x):
        # get the left digit of x, and then remove it
        # remainder is the remainder of x/base
        remainder = int(string_x[-p])
        # if the remainder is bigger than or equal to base
        if remainder >= base:
            # remainder >= base, so we have to carry one more digit
            result = str(remainder // base) + result
        else:
            # remainder < base, we don't have to carry
            result = str(remainder) + result
        # we move to the next digit by multiplying by base
        p = p * 10
    # test if x is negative
    if x >= 0:
        pass
    else:
        result = '-' + result
    return result
