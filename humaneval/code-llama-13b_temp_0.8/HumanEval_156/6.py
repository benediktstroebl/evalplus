
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
    thousands = number // 1000
    hundreds = number % 1000 // 100
    tens = number % 100 // 10
    ones = number % 10

    roman += 'm' * thousands
    if hundreds > 0:
        roman += 'c'
    roman += 'd' * hundreds
    if tens == 5:
        roman += 'l'
    elif tens == 9:
        roman += 'x'
        roman += 'i' * ones
    else:
        if tens > 5:
            roman += 'd'
            tens -= 5
        roman += 'c' * tens
        if ones > 0:
            roman += 'i' * ones
    return roman

