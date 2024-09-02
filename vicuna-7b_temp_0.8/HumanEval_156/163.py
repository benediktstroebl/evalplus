
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
    roman = []
    numeral = []
    while number > 0:
        if number % 1000 == 0:
            numeral.append(str(number % 1000))
        if number % 100 == 0:
            numeral.append(str(number % 100))
        if number % 10 == 0:
            numeral.append(str(number % 10))
        number = number / 10
        roman.append(str(int(number)))
    return ''.join(roman) + ''.join(numeral)
