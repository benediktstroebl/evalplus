

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
    # |num| is the input number
    # |base_num| is the base we want to change to
    # |result| is the output string
    # |base_str| is a string containing the symbols of the base (from 0 to base-1)
    num = abs(x)
    base_num = abs(base)
    if num < base_num:
        return str(num)
    base_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:base_num]
    result = ''
    while num > 0:
        remainder = num % base_num
        num = num // base_num
        result = base_str[remainder] + result
    if x < 0:
        result = '-' + result
    return result

