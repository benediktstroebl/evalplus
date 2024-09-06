

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

    if x == 0:
        return '0'
    if base > 10 or base < 2:
        raise ValueError("The base should be less than 10 and greater than 1")
    # set new_x to x
    new_x = x
    result = ''
    while new_x != 0:
        # append the remainder to result
        result = str(new_x % base) + result
        # new_x divides base
        new_x //= base
    return result

