
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
    if number < 1 or number > 1000:
        return ''
    roman_numeral = ''
    tens = 10
    hundreds = 100
    thousands = 1000
    while number > 0:
        if number - tens > 0:
            roman_numeral += 'x'
            number -= tens
        elif number - hundreds > 0:
            roman_numeral += 'c'
            number -= hundreds
        elif number - thousands > 0:
            roman_numeral += 'm'
            number -= thousands
        else:
            roman_numeral += 'i'
            number -= 1
    return roman_numeral.lower()

