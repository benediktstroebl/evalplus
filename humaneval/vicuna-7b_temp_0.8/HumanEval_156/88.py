
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
    if number >= 1000:
        roman_numeral = str(number)[-3:]
    elif number >= 900:
        roman_numeral = str(number)[-2:]
    elif number >= 800:
        roman_numeral = str(number)[-1:]
    else:
        if number >= 700:
            roman_numeral = str(number)[-1:]
        elif number >= 600:
            roman_numeral = str(number)[-2:]
        elif number >= 500:
            roman_numeral = str(number)[-3:]
        else:
            if number >= 400:
                roman_numeral = str(number)[-4:]
            elif number >= 300:
                roman_numeral = str(number)[-3:]
            elif number >= 200:
                roman_numeral = str(number)[-2:]
            else:
                if number >= 100:
                    roman_numeral = str(number)[-1:]
    return roman_numeral.lower()
