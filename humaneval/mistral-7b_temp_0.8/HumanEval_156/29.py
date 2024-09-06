
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
    # Write your code here.
    if number < 1 or number > 1000:
        raise ValueError("number must be between 1 and 1000")
    roman_values = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }
    roman_values_reversed = {value: key for key, value in roman_values.items()}
    roman_numeral = ''
    while number > 0:
        numeral_to_use = ''
        value = roman_values_reversed[min(number, 1000)]
        numeral_to_use += value
        number -= value
        if number >= value:
            roman_numeral += numeral_to_use
    return roman_numeral

