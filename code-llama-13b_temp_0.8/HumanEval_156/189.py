
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
    if not 1 <= number <= 1000:
        raise ValueError('number must be between 1 and 1000')

    int_to_roman = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm',
    }

    # loop through the dictionary in reverse order, since if we loop through in
    # order, we run into issues like 621 -> mxlxci, when 621 -> mlxxci would be
    # expected
    roman_str = ''
    for num, roman_num in sorted(int_to_roman.items(), reverse=True):
        if number < num:
            continue
        roman_str += roman_num * (number // num)
        number -= num * (number // num)

    return roman_str.lower()

