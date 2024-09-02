
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
    int_to_roman = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }

    roman_numerals = []
    divisor = 1

    while number > 0:
        quotient, remainder = divmod(number, divisor)
        if remainder == 0:
            roman_numerals.append(int_to_roman[divisor] * quotient)
            number -= quotient * divisor
            divisor *= 10
        else:
            number -= remainder
            roman_numerals.append(int_to_roman[remainder])
            divisor *= 10

    return ''.join(roman_numerals)

