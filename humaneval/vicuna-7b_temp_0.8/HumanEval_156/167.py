
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
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    numeral = str(number)

    if numeral.startswith('1'):
        numeral = numeral[1:]
    if numeral.startswith('2'):
        numeral = numeral[1:]
    if numeral.startswith('3'):
        numeral = numeral[1:]
    if numeral.startswith('4'):
        numeral = numeral[1:]
    if numeral.startswith('5'):
        numeral = numeral[1:]
    if numeral.startswith('6'):
        numeral = numeral[1:]
    if numeral.startswith('7'):
        numeral = numeral[1:]
    if numeral.startswith('8'):
        numeral = numeral[1:]
    if numeral.startswith('9'):
        numeral = numeral[1:]

    numeral_len = len(numeral)

    for digit, roman in roman_numerals.items():
        if numeral_len == 1:
            return roman
        elif numeral_len == 2 and numeral[0] == digit:
            return roman + numeral[1]
        elif numeral_len == 3 and numeral[0] == digit:
            return roman + numeral[1]
        elif numeral_len == 4 and numeral[0] == digit:
            return roman + numeral[1]
        elif numeral_len == 5 and numeral[0] == digit:
            return roman + numeral[1]
        elif numeral_len == 6 and numeral[0] == digit:
            return roman + numeral[1]
        elif numeral_
