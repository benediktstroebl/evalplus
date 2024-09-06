
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
    roman_numeral = ''
    if number < 40:
        roman_numeral = 'I' * number
    elif number < 50:
        roman_numeral = 'V' + 'I' * (number - 5)
    elif number < 100:
        roman_numeral = 'X' + 'I' * (number - 10)
    elif number < 150:
        roman_numeral = 'L' + 'X' * (number - 50)
    elif number < 200:
        roman_numeral = 'C' + 'X' * (number - 100)
    elif number < 250:
        roman_numeral = 'D' + 'C' * (number - 200)
    elif number < 500:
        roman_numeral = 'M' + 'C' * (number - 200)
    elif number < 600:
        roman_numeral = 'D' + 'C' * (number - 250)
    
