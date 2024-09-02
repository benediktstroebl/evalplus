
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
    roman_numeral = []
    while number > 0:
        if number == 1000:
            roman_numeral.append('M')
            number -= 1000
        elif number == 900:
            roman_numeral.append('CM')
            number -= 900
        elif number == 500:
            roman_numeral.append('D')
            number -= 500
        elif number == 400:
            roman_numeral.append('CD')
            number -= 400
        elif number >= 100:
            for i in range(number//100):
                roman_numeral.append('C')
            number -= number//100 * 100
        elif number >= 90:
            for i in range(number//90):
                roman_numeral.append('XC')
            number -= number//90 * 90
        elif number >= 50:
            for i in range(number//50):
                roman_numeral
