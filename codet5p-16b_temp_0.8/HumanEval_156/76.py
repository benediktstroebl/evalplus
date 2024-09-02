
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

    dict_numerals = {
        1: 'x', 2: 'cc', 3:'mmm', 4: 'vv', 5: 'v', 6: 'ii', 7: 'ii', 8: 'rr', 9: 'll',
        10: 'x', 20: 'cc', 30:'mm', 40: 'vv', 50: 'v', 60: 'ii', 70: 'ii', 80: 'rr', 90: 'll'
    }
    string = ''
    number_remainder = number
    for i in range(1, 10):
        value_possibilities = int(number_remainder / i)
        if value_possibilities == 9:
            if number_remainder / i == 9:
                string += dict_numerals[i] + dict_numerals[i+1] + dict_numerals[i+2]
                number_remainder = number_remainder - (9 * i) - (9 * (i + 1)) - (9 * (i + 2))
            else:
                string += dict_numerals
