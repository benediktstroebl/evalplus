
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

    # 0 1 2 3 4 5 6 7 8 9
    # I I I I I I I I I I I
    # X X X X X X X X X X X X
    # C C C C C C C C C C C C
    # M M M M M M M M M M M M
    roman_base = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    roman_numerals = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    roman = ''
    for power, value in roman_base.items():
        if number >= power:
            roman += value * (number // power)
            number %= power
    return roman

