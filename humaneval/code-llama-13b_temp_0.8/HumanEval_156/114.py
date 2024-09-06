
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
    units = ['i', 'x', 'c', 'm']
    tens = ['v', 'l', 'd']
    roman = ''
    for i in range(0, 4):
        roman += units[i] * (number % 10)
        number //= 10
    for i in range(0, 3):
        if (number % 5 == 4):
            roman = tens[i] + units[i + 1] + roman
        else:
            roman = tens[i] * (number % 5) + roman
        number //= 5
    return roman.lower()

