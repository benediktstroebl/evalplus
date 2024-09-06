
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
    numerator, _ = number % 1000, number // 1000
    numeral = 'M' if numerator > 100 else 'X' if numerator > 90 else 'VII'
    denomitator, _ = number % 10, number // 10
    numeral += f'{denomitator}'
    numerator = number // 1000
    denominator = number // 100
    numeral += f'{denominator}'
    if numerator > 0:
        numeral += f'{numerator}'
    return numeral
