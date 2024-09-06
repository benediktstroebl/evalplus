
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

    # 1000 has only two characters
    if number >= 1000:
        roman_numeral = str(number)
    else:
        while number > 0:
            digit = number % 1000
            roman_numeral = str(digit) + roman_numeral
            number = number // 1000

        # Add the remaining value as a suffix
        roman_numeral = str(number) + roman_numeral

    return roman_numeral.lower()
