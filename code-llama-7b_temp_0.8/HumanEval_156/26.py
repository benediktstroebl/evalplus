
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
    if number <= 0:
        raise ValueError("Input number must be positive")
    if number > 1000:
        raise ValueError("Input number must be <= 1000")
    
    roman_numeral_dictionary = {
        1000: "m",
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
        1: "i"
    }

    roman_numeral = ""
    for key in roman_numeral_dictionary.keys():
        roman_numeral_divisor = number // key
        if roman_numeral_divisor > 0:
            roman_numeral += roman_numeral_divisor * roman_numeral_dictionary[key]
            number -= roman_numeral_divisor * key

    return roman_numeral.lower()





















