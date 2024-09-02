

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
    # convert string to list of integers (with base)
    x = str(x)
    nums = []
    # for one digit
    if len(x) == 1:
        nums.append(int(x))
    # for two digits
    elif len(x) == 2:
        nums.append(int(x[0]))
        nums.append(int(x[1]))
    # for three digits
    elif len(x) == 3:
        nums.append(int(x[0]))
        nums.append(int(x[1]))
        nums.append(int(x[2]))
    # for four digits
    elif len(x) == 4:
        nums.append(int(x[0]))
        nums.append(int(x[1]))
        nums.append(int(x[2]))
        nums.append(int(x[3]))
    # for five digits
    elif len(x) == 5:
        nums.append(int(x[0]))
        nums.append(int(x[1]))
        nums.append(int(x[2]))
        nums.append(int(x[3]))
        nums.append(int(x[4]))
    # for 6 digits
    elif len(x) == 6:
        nums.append(int(x[0]))
        nums.append(int(x[1]))
        nums.append(int(x[2]))
        nums.append(int(x[3]))
        nums.append(int(x[4]))
        nums.append(int(x[5]))
    # for seven digits
    elif len(x) == 7:
        nums.append(int(x[0]))
        nums.append(int(x[1]))
        nums.append(int(x[2]))
        nums.append(int(x[3]))
        nums.append(int(x[4]))
        nums.append(