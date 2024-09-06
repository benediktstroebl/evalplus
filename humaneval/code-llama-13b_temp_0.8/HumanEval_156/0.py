
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
    numbers_map = {
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

    number_str = str(number)
    result = ''

    for i in range(1, len(number_str) + 1):
        digit = int(number_str[len(number_str) - i])
        previous_digit = int(number_str[len(number_str) - i - 1]) if i > 1 else 0
        power_of_ten = 10 ** (i - 1)
        prefix = numbers_map[power_of_ten]
        suffix = numbers_map[power_of_ten * 10] if power_of_ten * 10 in numbers_map else ''
        number_value = digit + power_of_ten * previous_digit
        roman_number = numbers_map[number_value] if number_value in numbers_map else prefix + suffix * (digit - 5)
        result = roman_number + result

    return result

