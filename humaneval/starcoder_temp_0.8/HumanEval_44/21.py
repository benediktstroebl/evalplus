

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
    # check whether x is an integer or not
    if not isinstance(x, int):
        raise TypeError("x must be an integer!")
    # check whether base is an integer or not
    if not isinstance(base, int):
        raise TypeError("base must be an integer!")
    # check whether base is less than 10
    if base >= 10:
        raise ValueError("base must be less than 10!")

    # check whether x is zero
    if x == 0:
        return '0'

    # set up a stack to store result
    result = []
    # check whether x is less than base
    while x > 0:
        # append the remainder onto the stack
        result.append(x % base)
        # remove the digits in the quotient
        x = x // base
    # reverse the stack and convert to string
    return ''.join(str(i) for i in result[::-1])

