

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
    # base numbers are less than 10
    assert base > 0 and base < 10
    # change number to string
    s = str(x)
    # result after the change
    result = ""
    # loop for each digit in s
    for c in s:
        # get the index in the current base
        i = int(c)
        # convert to the target base
        result += chr(ord("0") + i * base)
    # return the result
    return result
