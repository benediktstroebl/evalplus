
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
    num_to_roman_dict = {
        1: 'i',
        5: 'iv',
        10: 'v',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }

    raw_number_str = str(number)
    number_str = raw_number_str.zfill(len(raw_number_str))

    number_str_list = list(number_str)
    number_int_list = [int(i) for i in number_str_list]
    roman_str = ''

    for number, roman in num_to_roman_dict.iteritems():
        if number in number_int_list:
            index = number_int_list.index(number)
            roman_str += roman * number_int_list[index]

    return roman_str.lower()

