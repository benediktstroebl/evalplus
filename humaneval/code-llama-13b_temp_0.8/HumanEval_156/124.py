
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
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }
    result = []
    for digit in str(number)[::-1]:
        digit = int(digit)
        if digit == 0:
            continue
        elif digit < 4:
            result.append(mapping[1] * digit)
        elif digit == 4:
            result.append(mapping[1] + mapping[5])
        elif digit < 9:
            result.append(mapping[5] + mapping[1] * (digit - 5))
        elif digit == 9:
            result.append(mapping[1] + mapping[10])
    return ''.join(result[::-1])

