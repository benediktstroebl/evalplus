
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

    roman_dict = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }

    roman_nums = []

    for (value, roman) in roman_dict.items():
        roman_nums.append((value, roman))

    roman_nums = reversed(roman_nums)

    output = ''

    for (value, roman) in roman_nums:
        number_of_value = int(number / value)

        if number_of_value == 0:
            continue

        output += (roman * number_of_value)

        number = number - (number_of_value * value)

    return output

