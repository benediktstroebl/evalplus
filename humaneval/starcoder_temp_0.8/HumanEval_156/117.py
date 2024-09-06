
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
    numeral = ''
    for i in reversed(range(4)):
        if (number // (10 ** i)) == 9:
            numeral += 'ix'
        elif (number // (10 ** i)) >= 5:
            numeral += 'iv'
            number -= (10 ** i) * 5
        elif (number // (10 ** i)) >= 4:
            numeral += 'iv'
            number -= (10 ** i) * 4
        elif (number // (10 ** i)) >= 3:
            numeral += 'iii'
            number -= (10 ** i) * 3
        elif (number // (10 ** i)) >= 2:
            numeral += 'ii'
            number -= (10 ** i) * 2
        elif (number // (10 ** i)) >= 1:
            numeral += 'i'
            number -= (10 ** i) * 1
    return numeral
