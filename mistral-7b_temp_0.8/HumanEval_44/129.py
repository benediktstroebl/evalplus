

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
    num_str = str(x)
    num_str = num_str[::-1]
    result = ''
    for num in num_str:
        result += str(int(num) + base)
    return result[::-1]

