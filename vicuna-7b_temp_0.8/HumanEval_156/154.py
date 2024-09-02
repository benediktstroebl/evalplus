
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
    roman = ''
    while number > 0:
        numeral, modulo = number // 1000, number % 1000
        if numeral == 1000:
            roman = 'M' + roman
        elif numeral == 900:
            roman = 'CM' + roman
        elif numeral == 500:
            roman = 'D' + roman
        elif numeral == 400:
            roman = 'CD' + roman
        elif numeral == 100:
            roman = 'C' + roman
        elif numeral == 90:
            roman = 'XC' + roman
        elif numeral == 50:
            roman = 'L' + roman
        elif numeral == 40:
            roman = 'XL' + roman
        elif numeral == 10:
            roman = 'X' + roman
        else:
            roman = 'I' + roman
        number = modulo
    return roman
