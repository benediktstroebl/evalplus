
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
    mapping = {
        1 : 'i',
        2 : 'x',
        3 : 'c',
        4 : 'l',
        5 : 'v',
        6 : 'd',
        7 : 'm'
    }

    result = []
    number_mapping = {
        1 : 'i',
        4 : 'i',
        5 : 'v',
        9 : 'i',
        10 : 'x',
        40 : 'x',
        50 : 'l',
        90 : 'x',
        100 : 'c',
        400 : 'c',
        500 : 'd',
        900 : 'c',
        1000 : 'm'
    }
    number_mapping_values = number_mapping.values()

    for key,value in number_mapping.items():
        if number % key == 0:
            result.append(number_mapping[key])
            number = number - key

    for num in result:
        if num in number_mapping_values:
            number = number - num
        else:
            continue

    return str(number).lower()
