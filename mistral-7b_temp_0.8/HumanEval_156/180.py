
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
    if number < 1 or number > 1000:
        raise ValueError("The input is not a valid positive integer.")
    roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                      90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
                      4: 'IV', 1: 'I'}
    roman_str = ''
    for key, value in roman_numerals.items():
        while number >= key:
            roman_str += value
            number -= key
    return roman_str

