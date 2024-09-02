
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
    roman = {}
    roman['M'] = 1000
    roman['D'] = 500
    roman['C'] = 100
    roman['L'] = 50
    roman['X'] = 10
    roman['V'] = 5
    roman['I'] = 1

    res = []
    n = number

    if n >= 1000:
        n -= 1000
        res.append('M')

    if n >= 500:
        n -= 500
        res.append('D')

    if n >= 100:
        n -= 100
        res.append('C')

    if n >= 50:
        n -= 50
        res.append('L')

    if n >= 10:
        n -= 10
        res.append('X')

    if n >= 5:
        n -= 5
        res.append('V')

    if n >= 1:
        n -=
