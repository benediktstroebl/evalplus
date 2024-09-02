

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
    assert 2 <= base <= 16, "base can only be between 2 and 16, inclusive"
    # When x is 0, return the empty string.
    if x == 0:
        return ""
    # Convert base 10 to base 16 (and the reverse).
    digs = "0123456789ABCDEF"
    teens = "0123456789"
    def helper(x: int, base: int):
        """helper function."""
        if base == 16:
            return digs[x]
        else:
            return (teens[(x // base) % 10] + helper(x // base, base))
    res = helper(abs(x), base)
    if x < 0:
        return '-' + res
    else:
        return res

