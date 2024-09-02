
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
    if number <= 0:
        raise ValueError('Must be 1 or greater')
    if number < 4:
        return roman_list[number]
    if number < 9:
        return roman_list[5] + roman_list[number - 5]
    if number < 40:
        return roman_list[10] + roman_list[number - 10]
    if number < 50:
        return roman_list[50] + roman_list[number - 50]
    if number < 90:
        return roman_list[50] + roman_list[90 - number]
    if number < 400:
        return roman_list[100] + roman_list[number - 100]
    if number < 500:
        return roman_list[500] + roman_list[number - 500]
    if number < 900:
        return roman_list[500] + roman_list[900 - number]
    if number < 
