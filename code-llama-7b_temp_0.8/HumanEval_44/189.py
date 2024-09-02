

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
    # the number 0, which is represented by the empty list.
    zeros = ()
    # a helper function that takes a number x and returns the remainder
    # and the quotient when x is divided by base.
    def divmod_base(x):
        if x < base:
            return x, zeros
        else:
            return divmod_base(x // base) + (x % base,)
    # apply the helper function, then reverse the result to obtain the correct order
    return ''.join(map(str, divmod_base(x)[1][::-1]))

