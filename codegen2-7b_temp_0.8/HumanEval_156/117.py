
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
    conversion_table = {1: "i", 5: "v", 10: "x"}
    roman_numeral = ""
    while number > 0:
        for key, value in conversion_table.items():
            if number >= key:
                roman_numeral += value
                number -= key
                break
        number -= 1
    return roman_numeral.lower
