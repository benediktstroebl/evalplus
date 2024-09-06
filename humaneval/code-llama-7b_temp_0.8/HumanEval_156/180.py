
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

    # roman numerals are used to count 
    # how much to add to the parenthesis
    # key: integer value, value: roman numeral
    roman_numerals = {
        1000: 'm',
        500: 'd',
        100: 'c',
        50: 'l',
        10: 'x',
        5: 'v',
        1: 'i'
    }

    # only loop through the values in the
    # roman_numerals dictionary
    # if the number is 1000, then we only loop through
    # values up to 1000
    # then, we use the - function
    # to calculate how much to add to the parenthesis
    # ex: 426 = 400 + 20 + 6
    # so 400 is the first value, then we subtract
    # 400 to get 26 (which is 20 + 6)
    for value in roman_numerals.values():
        if number >= 1000:
            if number // 1000 * value != 0:
                return int_to_mini_roman(number // 1000) + value

        if number >= 100 and number // 100 * value != 0:
            return int_to_mini_roman(number // 100) + value

        if number >= 10 and number // 10 * value != 0:
            return int_to_mini_roman(number // 10) + value

        if number >= 1 and number // 1 * value != 0:
            return int_to_mini_roman(number // 1) + value

    return ''
