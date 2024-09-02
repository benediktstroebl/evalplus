
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

    ones_lookup = {1: "i", 5: "v", 10: "x"}
    fives_lookup = {1: "l", 5: "xl", 10: "xx"}
    tens_lookup = {1: "c", 5: "cl", 10: "l"}
    hunds_lookup = {1: "m", 5: "m"}
    hundreds_lookup = {
        1: "c",
        5: "cd",
        10: "d",
        50: "d",
        100: "m",
        500: "m",
    }
    thousands_lookup = {
        1: "m",
        5: "k",
        10: "m",
        50: "m",
        100: "b",
        500: "b",
        1000: "t",
    }
    num_lookup = {
        1000: "t",
        900: "cm",
        500: "d",
        400: "cd",
        100: "c",
        90: "xc",
        50: "l",
        40: "xl",
        10: "x",
        9: "ix",
        5: "v",
        4: "iv",
        1: "i",
    }

    if number > 3000:
        raise ValueError("Number must be below 3000")

    roman_numeral = ""
    thousands = int(number / 1000)
    if thousands > 0:
        roman_numeral += thousands_lookup[thousands] * thousands
        number %= 1000

    hundreds = int(number / 100)
    if hundreds > 0:
        roman_numeral += hundreds_lookup[hundreds]
        number %= 100

    tens = int(number / 10)
    if tens > 0:
        if tens == 9:
            roman_numeral += ones_lookup[1]
