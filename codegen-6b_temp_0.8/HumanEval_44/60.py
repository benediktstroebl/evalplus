

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
    x = str(x)
    digit = []
    for i in x:
        digit.append(i)
    while len(digit) < base:
        digit.append('0')
    alph = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if digit[0] not in alph:
        raise ValueError("enter a number")
    n = len(digit)
    c = 0
    a = []
    while c < n:
        if digit[c] in alph:
            index = alph.index(digit[c])
            a.append(index)
            c += 1
        else:
            c += 1
    a.reverse()
    i = 0
    while i < len(a):
        if a[i] >= 10:
            a[i] += 47
        i += 1
    a = [str(i) for i in a]
    a.reverse()
    a = ''.join(a)
    return a
