

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
    # TODO: Implement this function
    # ================ YOUR CODE HERE ==================
    if x<0:
        return "Error: Input is negative"

    if base<2 or base>10:
        return "Error: base is not valid"

    res = ''
    while x:
        x, mod = divmod(x, base)
        res += str(mod)

    return res[::-1]

