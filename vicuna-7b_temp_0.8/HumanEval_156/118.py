
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
    while number >= 1000:
        roman_numeral.append(str(number % 1000).zfill(2))
        number /= 1000
    if number == 0:
        return 'I'
    elif number == 1:
        return 'I'
    elif number == 2:
        return 'II'
    elif number == 3:
        return 'III'
    elif number == 4:
        return 'IV'
    elif number == 5:
        return 'V'
    elif number == 6:
        return 'VI'
    elif number == 7:
        return 'VII'
    elif number == 8:
        return 'VIII'
    elif number == 9:
        return 'IX'
    else:
        roman_numeral.append(str(number % 100).zfill(2))
        number /= 100
        if number == 0:
            return 'X'
        elif number == 11:
            return 'XI'
        elif number == 12:
            return 'XII'
        elif number == 13:
            return 'XIII'
        elif number == 14:
            return 'XIV'
        elif number == 15:
            return 'XV'
        elif number == 16:
            return 'XVI'
        elif number == 17:
            return 'XVII'
        elif number == 18:
            return 'XVIII'
        elif number == 19:
            return 'XIX'
        elif number == 20:
            return 'XX'
        elif number == 21:
            return 'XXI'
        elif number == 22:
            return 'XXII'
        elif number == 23:
            return 'XXIII'
        elif number == 24:
            return 'XXIV'
        elif number == 25:
            return 'XXV'
        elif number == 26:
            return 'XXVI'
        elif number == 27:
            return 'XX
