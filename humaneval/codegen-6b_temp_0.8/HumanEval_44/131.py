

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
    
    # check whether input is valid or not
    if isinstance(x, int) is False or isinstance(base, int) is False:
        raise TypeError

    # check whether input base is valid or not
    if base < 2 or base > 36:
        raise ValueError

    b_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if x < 0:
        is_negative = True
        x = -x
    else:
        is_negative = False

    new_base_num = []
    remainder = x
    while True:
        if remainder == 0:
            break
        digit = remainder % base
        new_base_num.append(b_str[digit])
        remainder = remainder // base

    # if input is negative, put '-' at the front of new_base_str
    new_base_str = ""
    if is_negative:
        new_base_str = "-"

    for i in range(len(new_base_num) - 1, -1, -1):
        new_base_str += new_base_num[i]

    return new_base_str


