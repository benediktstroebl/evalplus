
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
    # build the numerals
    numerals = {1: 'i',
                5: 'v',
                10: 'x',
                50: 'l',
                100: 'c',
                500: 'd',
                1000: 'm'}

    def _zeros_count(number):
        i = 0
        while number % 10 == 0:
            number //= 10
            i += 1
        return i

    # work backwards from the number
    roman = ''
    while number > 0:
        remainder = number % 1000
        # print(remainder)
        # rem = remainder // 1000
        # print(rem)
        # print('remainder // 1000: %d' % (remainder // 1000))
        # print('remainder % 1000: %d' % (remainder % 1000))
        # print('numerals[1000]: %s' % (numerals[1000]))
        # print('int(numerals[1000]): %s' % (int(numerals[1000])))
        if remainder >= 900:
            roman += numerals[1000]
            number -= 1000
        elif remainder >= 500:
            roman += numerals[500]
            number -= 500
        elif remainder >= 400:
            roman += numerals[100] * (_zeros_count(remainder) - 1)
            number -= 400
        elif remainder >= 100:
            roman += numerals[100] * _zeros_count(remainder)
            number -= 100
        elif remainder >= 90:
            roman += numerals[90]
            number -= 90
        elif remainder >= 50:
            roman += numerals[50]
            number -= 50
        elif remainder >= 40:
            roman += numerals[40] * (_zeros_count(remainder) - 1)
            number -= 40
        elif remainder >= 10:
            roman += numerals[10] * _zeros_count(remainder)
            number -= 10
        elif remainder >= 9:
            roman += numerals[9]
            number -= 9
        else:
            roman += numerals[remainder]
