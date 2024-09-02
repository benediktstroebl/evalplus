
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
    roman = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }
    result = ''
    key = list(roman.keys())[::-1]
    num = str(number)
    num_list = [int(n) for n in num]

    for i, n in enumerate(num_list):
        if n in key:
            result += roman[n] * n
        elif n + num_list[i + 1] in key:
            result += roman[n + num_list[i + 1]]
        else:
            break
    return result
