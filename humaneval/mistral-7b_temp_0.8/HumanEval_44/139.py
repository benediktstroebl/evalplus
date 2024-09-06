

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
    # check if x is in range
    if x < 0 or x > 9:
        return "number is not in range"
    # check if base is in range
    if base < 2 or base > 9:
        return "base is not in range"
    # create a list of digits for x and base
    digits = []
    # create a list of digits for x and base
    digit_base = []
    # convert x to digits list
    while x > 0:
        # get the last digit
        digit = x % base
        # add digit to digits list
        digits.append(digit)
        # divide x by base
        x = x // base
    # convert base to digits list
    while base > 0:
        # get the last digit
        digit = base % 10
        # add digit to digit_base list
        digit_base.append(digit)
        # divide base by 10
        base = base // 10
    # convert digits list to string
    digit_str = ''.join
