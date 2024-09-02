
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
    roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    roman_values = [1, 5, 10, 50, 100, 500, 1000]

    if number < 1 or number > 1000:
        raise ValueError("Number must be between 1 and 1000")

    roman_number = ''
    for i in range(len(roman_numerals)):
        while number >= roman_values[i]:
            number -= roman_values[i]
            roman_number += roman_numerals[i]

    return roman_number
