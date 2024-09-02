
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

    roman = {
        1: 'x',
        4: 'ix',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xix',
        50: 'v',
        90: 'xci',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000:'m',
    }
    if 1 <= number <= 1000:
        ret = ""
        for n in range(1, number + 1):
            if n == 1:
                ret += roman[n]
            elif n >= 5:
                ret += roman[n]
                if n == 9:
                    ret += roman[n]
                elif n == 10:
                    ret += roman[n]
                elif n == 40:
                    ret += roman[n]
                elif n == 50:
                    ret += roman[n]
                elif n == 90:
                    ret += roman[n]
                elif n == 100:
                    ret +=
