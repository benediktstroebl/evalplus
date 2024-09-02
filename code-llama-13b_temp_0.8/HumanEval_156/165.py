
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
    roman_dict = {
        1: "i",
        5: "v",
        10: "x",
        50: "l",
        100: "c",
        500: "d",
        1000: "m",
    }
    roman_numeral = ""
    next_numeral = 1000
    next_numeral_value = 1000
    while number > 0:
        quotient = number // next_numeral
        number %= next_numeral
        if quotient == 4:
            roman_numeral += roman_dict[next_numeral] + roman_dict[next_numeral_value]
        elif quotient == 9:
            roman_numeral += roman_dict[next_numeral_value] + roman_dict[next_numeral]
        elif quotient >= 5:
            roman_numeral += roman_dict[next_numeral_value] * (quotient - 5)
            roman_numeral += roman_dict[next_numeral]
        else:
            roman_numeral += roman_dict[next_numeral] * quotient
        next_numeral_value = next_numeral
        next_numeral //= 10
    return roman_numeral.lower()

