

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
    
    if base > 10:
        raise ValueError('Base must be less than 10.')
    
    s = ''
    if base == 10:
        for digit in str(x):
            s += digit
    else:
        s = str(x)
    
    s = list(s)
    
    for i in range(len(s)):
        s[i] = chr(int(s[i])+ord('a')-1)
    
    
