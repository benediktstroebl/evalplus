

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

    def change_base_helper(x: int, base: int):
        """Convert int to base using recursion.
        >>> change_base_helper(8, 2)
        '1000'
        >>> change_base_helper(7, 2)
        '111'
        """
        if x == 0:
            return ''
        return change_base_helper(x // base, base) + str(x % base)
    return change_base_helper(x, base)


