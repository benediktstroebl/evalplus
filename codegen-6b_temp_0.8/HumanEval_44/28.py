

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
    if x == 0:
        return '0'
    elif x < 0:
        strr = '-'
        x = abs(x)
    else:
        strr = ''
    base_num = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
                'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
                'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24,
                'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
                'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34,
                'Z': 35}
    if x < base:
        return strr + str(x)
    else:
        return change_base(x//base, base) + str(base_num[x%base])

