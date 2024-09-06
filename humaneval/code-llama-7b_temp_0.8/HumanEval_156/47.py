
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

    roman_numerals = {
        1000: 'm',
        500: 'd',
        100: 'c',
        50: 'l',
        10: 'x',
        5: 'v',
        1: 'i',
    }

    int_list = str(number).split()
    int_list = [int(num) for num in int_list]
    int_list.reverse()

    roman_num = ''

    for num in int_list:
        if num >= 1000:
            num -= 1000
            roman_num += 'm' * num
        elif num >= 500:
            num -= 500
            roman_num += 'd'
            roman_num += 'c' * num
        elif num >= 100:
            num -= 100
            roman_num += 'c'
            roman_num += 'x' * num
        elif num >= 50:
            num -= 50
            roman_num += 'l'
            roman_num += 'x' * num
        elif num >= 10:
            num -= 10
            roman_num += 'x'
            roman_num += 'i' * num
        elif num >= 5:
            num -= 5
            roman_num += 'v'
            roman_num += 'i' * num
        elif num >= 1:
            roman_num += 'i' * num

    return roman_num

