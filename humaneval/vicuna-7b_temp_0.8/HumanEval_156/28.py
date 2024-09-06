
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
    roman_table = [
        'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'V', 'IV', 'I'
    ]

    roman_value = 0
    for value, numeral in enumerate(roman_table):
        if number >= value:
            roman_value += (number - value) / 100
    roman_value += number % 100
    roman_value = romans.to(roman_value, 4)
    return roman_value.lower()