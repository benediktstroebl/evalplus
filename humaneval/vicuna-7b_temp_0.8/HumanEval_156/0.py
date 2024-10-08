
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
        if number == 1:
            roman_numeral += "I"
        else:
            roman_numeral += number % 1000 + "C"
            number = number / 1000
    return roman_numeral.lower()
