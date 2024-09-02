
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
    roman = ''
    numerator = number // 1000
    unit = number - numerator * 1000
    tens = ''
    for i in range(1, numerator):
        tens += 'I'
    for i in range(1, unit):
        tens += 'V'
    for i in range(1, 1000):
        roman += 'X' * (1000 - i) if tens == 'V' else 'I' * (1000 - i)
    for i in range(1, unit):
        roman += 'IV' if tens == 'I' else 'V'
    return roman
