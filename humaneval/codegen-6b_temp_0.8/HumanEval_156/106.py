
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
    if number == 0:
        return ''
    num_to_roman = (
        (1000, 'm'),
        (900, 'CM'),
        (500, 'd'),
        (400, 'CD'),
        (100, 'c'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    )
    res = []
    for amount, roman in num_to_roman:
        res.append(number // amount * roman)
        number %= amount
    return ''.join(res).lower()

