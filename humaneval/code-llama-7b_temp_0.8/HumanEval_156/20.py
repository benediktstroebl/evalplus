
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
    # All roman numerals contain the letters I, X, C and M in the order
    # I, V, X, L, C, D, M, so we should check for those, then return
    # the corresponding roman numeral.
    if number < 1:
        raise ValueError("number must be a positive integer")

    roman_map = {
        1: "i",
        5: "v",
        10: "x",
        50: "l",
        100: "c",
        500: "d",
        1000: "m",
    }

    result = ""
    highest_roman = 1000
    while number > 0:
        if number >= highest_roman:
            result += roman_map[highest_roman]
            number -= highest_roman
        else:
            for roman_value, roman_letter in roman_map.items():
                if roman_value < number:
                    highest_roman = roman_value

    return result.lower()

