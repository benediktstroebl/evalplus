
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

    result = ""
    if number <= 0:
        return ""
    roman_number_dict = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }
    numerals_to_remove = []
    for key, value in roman_number_dict.items():
        while number >= key:
            result += value
            number -= key

    if number > 0:
        numerals_to_remove.append(1000)
        numerals_to_remove.append(500)
        numerals_to_remove.append(100)
        numerals_to_remove.append(50)
        numerals_to_remove.append(10)
        numerals_to_remove.append(5)
        numerals_to_remove.append(1)
    for i in numerals_to_remove:
        if number % i
