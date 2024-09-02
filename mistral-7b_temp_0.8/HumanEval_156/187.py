
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

    roman_num = ''
    if number <= 100:
        if number % 10 == 9:
            roman_num += 'ix'
            number -= 9
        elif number % 10 == 5:
            roman_num += 'v'
            number -= 5
        if number % 10 != 0:
            roman_num += 'I' * number % 10
            number -= number % 10

        if number % 100 == 90:
            roman_num += 'xc'
            number -= 90
        elif number % 100 == 50:
            roman_num += 'l'
            number -= 50
        if number % 100 != 0:
            roman_num += 'X' * number % 100 // 10
            number -= number % 100 // 10 * 10

        if number % 100 == 90:
            roman_num += 'xc'
            number -= 90
        elif number % 
