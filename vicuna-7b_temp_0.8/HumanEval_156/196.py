
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
    remainder = number % 10
    while number:
        if number % 100 == 0:
            roman = 'C' + roman + 'C'
        number = number / 100
        if remainder == 0:
            break
        remainder = remainder // 10
    for i in range(10):
        roman = 'X' + roman[::-1] if remainder == i else roman
    return roman
