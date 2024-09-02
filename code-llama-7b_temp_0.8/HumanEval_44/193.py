

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
    if x < 0:
        raise ValueError('x should be positive')

    def change_base_1(x: int, base: int, result: str):
        """Helper function.
        Return the string representation of number x in base.
        """
        if x == 0:
            return result
        change_base_1(x//base, base, result + str(x%base))
    return change_base_1(x, base, '')

