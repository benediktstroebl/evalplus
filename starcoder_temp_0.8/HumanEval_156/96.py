
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

    numeral_dict = {
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
        100: 'c',
        1000: 'M',
        500: 'd',
        10000: 'MMMM',
        5000: 'MMMMD'
    }

    output_string = ''

    for i in reversed(sorted(numeral_dict.keys())):
        while number > 0:
            if number >= i:
                output_string += numeral_dict[i]
                number -= i
            else:
                break

    return output_string

