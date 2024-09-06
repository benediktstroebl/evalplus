

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
    # Check if input x is negative
    if x < 0:
        x = -x

    # Get the number of leading zeros of base x
    n = 0
    while x > 0:
        x //= base
        n += 1

    # Get the number of trailing zeros of base x
    m = 0
    while base > 1:
        base //= 10
        m += 1

    # Get the result string
    result_str = ""
    for i in range(n + m):
        result_str = str(base) + result_str

    # Return the result string
    return result_str
