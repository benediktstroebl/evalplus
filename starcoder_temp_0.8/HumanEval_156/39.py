
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
    roman_numerals = {
        1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v', 6: 'vi', 7: 'vii', 8: 'viii', 9: 'ix',
        10: 'x', 20: 'xx', 30: 'xxx', 40: 'xl', 50: 'l', 60: 'lx', 70: 'lxx', 80: 'lxxx', 90: 'xc',
        100: 'c', 200: 'cc', 300: 'ccc', 400: 'cd', 500: 'd', 600: 'dc', 700: 'dcc', 800: 'dccc', 900: 'cm',
        1000: 'M', 2000: 'MM', 3000: 'MMM'
    }

    roman_numeral = ''
    if number < 1 or number > 3000:
        return None
    while number > 0:
        if number >= 1000:
            number -= 1000
            roman_numeral += 'M'
        elif number >= 900:
            number -= 900
            roman_numeral += 'CM'
        elif number >= 500:
            number -= 500
            roman_numeral += 'D'
        elif number >= 400:
            number -= 400
            roman_numeral += 'CD'
        elif number >= 100:
            number -= 100
            roman_numeral += 'C'
        elif number >= 90:
            number -= 90
            roman_numeral += 'XC'
        elif number >= 50:
            number -= 50
            roman_numeral += 'L'
        elif number >= 40:
            number -= 40
            roman_numeral += 'XL'
        elif number >= 10:
            number -= 10
            roman_numeral += 'X'
        elif number >= 9:
            number -= 9
            roman_numeral
