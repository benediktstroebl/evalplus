
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
    num_map = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}
    result = ''
    for k in range(len(num_map) - 1, 0, -1):
        result = num_map[k] * num_map[k * 10] + result
        if k > 5 and num_map[k] == 'i':
            result = num_map[k * 10 - 1] + result
    return result

