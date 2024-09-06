
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
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }

    if number <= 0:
        raise ValueError('number should be a positive integer.')

    def convert(num):
        if num in roman:
            return roman[num]
        elif num > 5 * max(roman.keys()):
            return convert(5 * max(roman.keys())) + convert(num - 5 * max(roman.keys()))
        else:
            for r in sorted(roman.keys(), reverse=True):
                if num >= r:
                    return roman[r] + convert(num - r)

    result = ''
    for n in [1000, 100, 10, 1]:
        result += convert(number // n)
        number %= n

    return result

