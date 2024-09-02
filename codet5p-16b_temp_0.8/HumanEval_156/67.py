
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

    
    roman_dict = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000:'m'
    }

    values = [1, 5, 10, 50, 100, 500, 1000]
    results = []

    for val in values:
        count, number = divmod(number, val)

        while count > 0:
            results.append(roman_dict[val])
            count -= 1

    return ''.join(results).lower()
