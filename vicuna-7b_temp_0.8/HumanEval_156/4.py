
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
    numeral = []
    while number >= 1000:
        numeral.append(f'{number // 1000:D}' if number % 1000 == 0 else f'{number // 1000:C}')
        number = number / 1000
    numeral.append(f'{number:D}' if number == 1000 else f'{number:C}')
    return ''.join(numeral)
