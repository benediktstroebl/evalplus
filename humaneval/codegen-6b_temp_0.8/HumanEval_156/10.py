
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
    mini_roman_numeral = ""
    while number > 0:
        if number >= 1000:
            numeral = number / 1000
            number -= numeral * 1000
            mini_roman_numeral += "M" * int(numeral)
        elif number >= 900:
            mini_roman_numeral += "CM"
            number -= 900
        elif number >= 500:
            numeral = number / 500
            number -= numeral * 500
            mini_roman_numeral += "D" * int(numeral)
        elif number >= 400:
            mini_roman_numeral += "CD"
            number -= 400
        elif number >= 100:
            numeral = number / 100
            number -= numeral * 100
            mini_roman_numeral += "C" * int(numeral)
        elif number >= 90:
            mini_roman_numeral += "XC"
            number -= 90
        elif number >= 50:
            numeral = number / 50
            number -= numeral * 50
            mini_roman_numeral += "L" * int(numeral)
        elif number >= 40:
            mini_roman_numeral += "XL"
            number -= 40
        elif number >= 10:
            numeral = number / 10
            number -= numeral * 10
            mini_roman_numeral += "X" * int(numeral)
        elif number >= 9:
            mini_roman_numeral += "IX"
            number -= 9
        elif number >= 5:
            numeral = number / 5
            number -= numeral * 5
            mini_roman_numeral += "V" * int(numeral)
        elif number >= 4:
            mini_roman_numeral += "IV"
            number -= 4
        elif number >= 1:
            numeral = number / 1
            number -= numeral * 1
            mini_roman_numeral += "I" * int(numeral)
    return mini_roman_numeral

