
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

    roman_numerals = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    list_numbers = []

    while number > 0:
        for number_value in roman_numerals:
            if number > number_value:
                number -= number_value
                list_numbers.append(roman_numerals[number_value])
                break
            else:
                list_numbers.append(roman_numerals[number_value])
                break
    return ''.join(list_numbers)

