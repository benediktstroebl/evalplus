
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
    if number >= 1000:
        roman = f'{number} CD'
    else:
        i = 2
        while number >= 10:
            roman += str(number // 10).zfill(1)
            number -= 10
            i -= 1
        roman += str(number).zfill(3)
    return roman.lower()
