
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    lst = []
    n = number
    while n:
        if n >= 1000:
            lst.append('m')
            n -= 1000
        elif n >= 900:
            lst.append('cm')
            n -= 900
        elif n >= 500:
            lst.append('d')
            n -= 500
        elif n >= 400:
            lst.append('cd')
            n -= 400
        elif n >= 100:
            lst.append('c')
            n -= 100
        elif n >= 90:
            lst.append('xc')
            n -= 90
        elif n >= 50:
            lst.append('l')
            n -= 50
        elif n >= 40:
            lst.append('xl')
            n -= 40
        elif n >= 10:
            lst.append('x')
            n -= 10
        elif n >= 9:
            lst.append('ix')
            n -= 9
        elif n >= 5:
            lst.append('v')
            n -= 5
        elif n >= 4:
            lst.append('iv')
            n -= 4
        elif n >= 1:
            lst.append('i')
            n -= 1

    return ''.join(lst)
