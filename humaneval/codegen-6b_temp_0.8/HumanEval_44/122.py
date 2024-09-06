

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
    # convert x to str
    x = str(x)
    # get length of str x
    lens = len(x)
    # change base, store result
    result = 0
    # multiple by base**(length-1)
    for i in range(lens):
        result += int(x[lens-1-i])*(base**(lens-1-i))
        # print(result)
    # convert result to str
    result = str(result)
    return result
