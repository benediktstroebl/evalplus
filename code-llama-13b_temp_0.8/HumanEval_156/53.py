
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

    num_map = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix',
        10: 'x', 40: 'xl', 50: 'l', 90: 'xc',
        100: 'c', 400: 'cd', 500: 'd', 900: 'cm',
        1000: 'm'
    }

    result = ''
    power = 0
    while number:
        cur_num = (number % 10) * (10 ** power)

        if cur_num in num_map:
            result = num_map[cur_num] + result
        else:
            one = (cur_num % 10) * (10 ** (power - 1))
            five = ((cur_num % 100) - one) * (10 ** (power - 1))
            result = num_map[five] + num_map[one] + result

        number //= 10
        power += 1
    return result

