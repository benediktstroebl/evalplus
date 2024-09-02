

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

    
    def base_helper(x: int, base: int):
        """A helper function to implement change_base.
        >>> base_helper(8, 3)
        '22'
        >>> base_helper(8, 2)
        '1000'
        >>> base_helper(7, 2)
        '111'
        """
        
        base10_number = 0
        
        while x > 0:
            base10_number = base10_number + int(x % base) * (base ** base10_number)
            x = x // base
        
        return base10_number
    
    return change_base(base_helper(x, base), base)
