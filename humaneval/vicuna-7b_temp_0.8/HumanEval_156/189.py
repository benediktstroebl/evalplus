
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
        if number == 1:
            roman = 'I' + roman
        elif number == 2:
            roman = 'II' + roman
        elif number == 3:
            roman = 'III' + roman
        elif number == 4:
            roman = 'IV' + roman
        elif number == 5:
            roman = 'V' + roman
        elif number == 6:
            roman = 'VI' + roman
        elif number == 7:
            roman = 'VII' + roman
        elif number == 8:
            roman = 'VIII' + roman
        elif number == 9:
            roman = 'IX' + roman
        number //= 10
    return roman.lower()
