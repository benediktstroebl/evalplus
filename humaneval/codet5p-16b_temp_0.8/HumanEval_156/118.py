
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

    roman_numeral = ""
    while number > 0:
        if number >= 1000:
            roman_numeral = roman_numeral + "m"
            number -= 1000
        elif number >= 900:
            roman_numeral = roman_numeral + "cm"
            number -= 900
        elif number >= 500:
            roman_numeral = roman_numeral + "d"
            number -= 500
        elif number >= 400:
            roman_numeral = roman_numeral + "cd"
            number -= 400
        elif number >= 100:
            roman_numeral = roman_numeral + "c"
            number -= 100
        elif number >= 90:
            roman_numeral = roman_numeral + "xc"
            number -= 90
        elif number >= 50:
            roman_numeral = roman_numeral + "l"
            number -= 50
        elif number >= 40:
            roman_numeral = roman_numeral + "xl"
            number -= 40
        elif number >= 10:
            
