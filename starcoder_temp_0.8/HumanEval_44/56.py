

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
    # Use `str` to convert `x` to a string
    x_str = str(x)
    # initialize empty accumulator
    new_num = ""
    # loop over digits of x
    for i in range(len(x_str)):
        # use int and string indexing to extract the digit at position i.
        # add extracted digit to accumulator
        new_num = new_num + str(int(x_str[i], base))
    return new_num
