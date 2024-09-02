
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

    if not isinstance(number, int) or number < 1 or number > 1000:
        return 'ERROR: {} is not a valid integer'.format(number)

    mini_roman = ''
    roman_digits = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
    ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9),
    ('V', 5), ('IV', 4), ('I', 1)]

    for roman_digit in roman_digits:
        while number >= roman_digit[1]:
            mini_roman += roman_digit[0]
            number -= roman_digit[1]
    return mini_roman

