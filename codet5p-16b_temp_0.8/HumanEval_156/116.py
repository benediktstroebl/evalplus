
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

    assert 1 <= number <= 1000, "Invalid input!"
    thousend_check = number // 1000
    hundred_check = (number % 1000) // 100
    ten_check = (number % 100) // 10
    one_check = number % 10

    roman_numeral = ''

    if thousend_check == 9:
        roman_numeral += 'CM'
    elif thousend_check == 8:
        roman_numeral += 'DCCC'
    elif thousend_check == 7:
        roman_numeral += 'DCC'
    elif thousend_check == 6:
        roman_numeral += 'DC'
    elif thousend_check == 5:
        roman_numeral += 'D'

    if hundred_check == 9:
        roman_numeral += 'CMM'
    elif hundred_check == 8:
        roman_numeral += 'MMM'
    elif hundred_check == 7:
        roman_numeral += 'MM'
    elif hundred_check == 6:
        roman_numeral += 'M'
    
