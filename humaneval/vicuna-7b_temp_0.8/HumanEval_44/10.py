

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
    # check base
    if base <= 9:
        # convert to base 10
        return str(int(x) // (10**(9-base))) + (int(x) % (10**(9-base))).to_base(base)
    else:
        # convert to base 10
        return str(int(x) // (10**(base-10))) + (int(x) % (10**(base-10)))