
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
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    roman_numeral_values = sorted(roman_numerals.values(), reverse=True)
    roman_numeral_letters = [
        roman_numeral
        for roman_numeral, value in roman_numerals.items()
        if value in roman_numeral_values
    ]
    roman_numeral_strings = [
        roman_numeral_string
        for roman_numeral_letter in roman_numeral_letters
        for roman_numeral_string in [
            roman_numeral_letter * count
            for count in range(1, (number // value) + 1)
        ]
    ]
    return ''.join(roman_numeral_strings).lower()
