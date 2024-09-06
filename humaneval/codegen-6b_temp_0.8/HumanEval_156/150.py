
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
    assert type(number) == int
    assert 1 <= number <= 1000
    #CONSTANTS
    ROMAN_NUMBERS = {
        1: 'i',
        2: 'ii',
        3: 'iii',
        4: 'iv',
        5: 'v',
        6: 'vi',
        7: 'vii',
        8: 'viii',
        9: 'ix',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }

    #BASE CONVERSIONS
    DIGITS = {
        0: '',
        1: 'i',
        2: 'ii',
        3: 'iii',
        4: 'iv',
        5: 'v',
        6: 'vi',
        7: 'vii',
        8: 'viii',
        9: 'ix'
    }

    if number in DIGITS:
        return DIGITS[number]
    elif number < 10:
        return DIGITS[number]

    #MAIN CONVERSION LOOP
    roman_numeral = ''
    while number > 0:
        fact = int(math.ceil(number/100.0))
        number = number % 100
        temp_roman = ROMAN_NUMBERS[fact]
        if num < 10:
            roman_numeral = DIGITS[num] + temp_roman
        elif num < 20:
            roman_numeral = temp_roman + DIGITS[num-10]
        elif num < 100:
            roman_numeral = DIGITS[num/10] + temp_roman
        else:
            roman_numeral = temp_roman + DIGITS[num%10]
        number = fact
    return roman_numeral.lower()
