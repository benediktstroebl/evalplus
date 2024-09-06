
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
    number_to_roman = {
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
        1000: 'm'
    }
    if number in number_to_roman:
        return number_to_roman[number]

    result = ''
    if number < 10:
        return result + number_to_roman[number % 10]
    if number < 40:
        result += number_to_roman[number // 10 * 10]
        result += number_to_roman[number % 10]
    elif number < 50:
        result += number_to_roman[number - 10]
        result += number_to_roman[10]
    elif number < 90:
        result += number_to_roman[number - 50]
        result += number_to_roman[50]
    elif number < 100:
        result += number_to_roman[number - 90]
        result += number_to_roman[90]
    elif number < 400:
        result += number_to_roman[number // 100 * 100]
        result += number_to_roman[number % 100]
    elif number < 500:
        result += number_to_roman[number - 400]
        result += number_to_roman[400]
    elif number < 900:
        result += number_to_roman[number - 500]
        result += number_to_roman[500]
    elif number < 1000:
        result += number_to_roman[number - 900]
        result
