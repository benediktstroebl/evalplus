
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

    assert isinstance(number, int) and number >= 1 and number <= 1000
    roman_numeral = ''
    arabic_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    if number == 1000:
        roman_numeral = 'M'
    elif number in arabic_numerals:
        roman_numeral = arabic_numerals[number]
    else:
        for key, val in arabic_numerals.items():
            if number >= key:
                roman_numeral += val
                number -= key
        roman_numeral += int_to_mini_roman(number)
    return roman_numeral.lower()
