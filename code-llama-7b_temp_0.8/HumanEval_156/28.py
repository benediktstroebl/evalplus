
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

    # I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
    # vowels = "aeiou"
    # consonants = "bcdfghjklmnpqrstvwxyz"

    # conversions = {
    #     1: "i",
    #     5: "v",
    #     10: "x",
    #     50: "l",
    #     100: "c",
    #     500: "d",
    #     1000: "m"
    # }

    # roman_numeral = []
    # for multiplier in conversions.keys():
    #     if number == 0:
    #         break
    #     if number >= multiplier:
    #         roman_numeral.append(conversions[multiplier])
    #         number -= multiplier
    # return "".join(roman_numeral)

    roman_numeral = []
    while number > 0:
        if number >= 1000:
            roman_numeral.append("m")
            number -= 1000
        elif number >= 500:
            roman_numeral.append("d")
            number -= 500
        elif number >= 100:
            roman_numeral.append("c")
            number -= 100
        elif number >= 50:
            roman_numeral.append("l")
            number -= 50
        elif number >= 10:
            roman_numeral.append("x")
            number -= 10
        elif number >= 5:
            roman_numeral.append("v")
            number -= 5
        elif number >= 1:
            roman_numeral.append("i")
            number -= 1
    return "".join(roman_numeral)

