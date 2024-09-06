

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
    if base < 10:
        # you know, if the base is less than 10, it's easy
        # just divide by the base and get the remainder
        return str(x % base)
    else:
        # if the base is not less than 10, divide the input number by the base
        # and get the remainder (as the number is non-negative)
        # then we can use recursion
        return change_base(x % base, base - 10)

