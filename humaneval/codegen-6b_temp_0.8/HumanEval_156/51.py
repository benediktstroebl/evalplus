
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
    if number > 1000 or number < 1:
        raise ValueError('Input must be between 1 and 1000 inclusive')

    roman_map = {1000: 'm', 900: 'CM', 500: 'd', 400: 'CD', 100: 'c', 90: 'XC',
                 50: 'l', 40: 'XL', 10: 'x', 9: 'IX', 5: 'v', 4: 'IV', 1: 'I'}

    result = ''
    for i in range(1, number + 1):
        if i in roman_map:
            result += roman_map[i]
        elif i % 100 == 0:
            result += roman_map[i // 100] + roman_map[100]
        elif i % 10 == 0:
            result += roman_map[i // 10 * 10] + roman_map[10]
        else:
            result += roman_map[i // 10] + roman_map[i % 10]
    return result.lower()

