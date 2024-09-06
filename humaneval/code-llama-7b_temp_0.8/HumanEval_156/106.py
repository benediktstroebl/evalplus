
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
    mini_roman = {
        (1000, 'm'): 0,
        (900, 'cm'): 1,
        (500, 'd'): 2,
        (400, 'cd'): 3,
        (100, 'c'): 4,
        (90, 'xc'): 5,
        (50, 'l'): 6,
        (40, 'xl'): 7,
        (10, 'x'): 8,
        (9, 'ix'): 9,
        (5, 'v'): 10,
        (4, 'iv'): 11,
        (1, 'i'): 12,
    }
    num = number
    roman = ''
    for val, rep in sorted(mini_roman, key=lambda x: -x[0]):
        while num >= val:
            num -= val
            roman += rep
    return roman.lower()
