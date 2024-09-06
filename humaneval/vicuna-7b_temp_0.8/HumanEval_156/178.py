
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
    if number == 1:
        roman_numeral = 'I'
    elif number == 2:
        roman_numeral = 'II'
    elif number == 3:
        roman_numeral = 'III'
    elif number == 4:
        roman_numeral = 'IV'
    elif number == 5:
        roman_numeral = 'V'
    elif number == 6:
        roman_numeral = 'VI'
    elif number == 7:
        roman_numeral = 'VII'
    elif number == 8:
        roman_numeral = 'VIII'
    elif number == 9:
        roman_numeral = 'IX'
    elif number >= 10 and number <= 39:
        roman_numeral = 'X'
        if number > 10:
            number -= 10
            roman_numeral += 'X'
        elif number < 10:
            roman_numeral += 'IX'
    elif number >= 40 and number <= 99:
        roman_numeral = 'XLIV'
        if number >= 100:
            number -= 100
            roman_numeral += 'XL'
            if number >= 400:
                number -= 400
                roman_numeral += 'XL'
            elif number >= 10:
                roman_numeral += 'X'
                if number > 10:
                    number -= 10
                    roman_numeral += 'X'
                elif number < 10:
                    roman_numeral += 'IX'
        else:
            roman_numeral += 'XL'
    elif number >= 100 and number <= 299:
        roman_numeral = 'C'
        if number >= 300:
            number -= 300
            roman_numeral += 'C'
            if number >= 400:
                number -= 400
                roman_numeral += 'CC'
            elif number >= 100:
                roman_numeral += 'CX'
