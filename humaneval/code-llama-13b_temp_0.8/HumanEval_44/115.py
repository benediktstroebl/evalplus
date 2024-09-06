

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
    base_chars = "0123456789ABCDEF"
    result = ""
    num = x
    while num >= base:
        result += base_chars[num%base]
        num = num//base
    result += base_chars[num%base]
    return result[::-1]
