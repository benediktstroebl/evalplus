
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
    res = ''
    while number > 0:
        if number >= 1000:
            res += 'M'
            number -= 1000
        elif number >= 900:
            res += 'CM'
            number -= 900
        elif number >= 500:
            res += 'D'
            number -= 500
        elif number >= 400:
            res += 'CD'
            number -= 400
        elif number >= 100:
            res += 'C'
            number -= 100
        elif number >= 90:
            res += 'XC'
            number -= 90
        elif number >= 50:
            res += 'L'
            number -= 50
        elif number >= 40:
            res += 'XL'
            number -= 40
        elif number >= 10:
            res += 'X'
            number -= 10
        elif number >= 9:
            res += 'IX'
            number -= 9
        elif number >= 5:
            res += 'V'
            number -= 5
        elif number >= 4:
            res += 'IV'
            number -= 4
        elif number >= 1:
            res += 'I'
            number -= 1
    return res.lower()

