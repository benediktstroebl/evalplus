
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

    if not (1 <= number <= 1000):
        raise ValueError(
            'Number must be between 1 and 1000 inclusive')
    roman_map = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000:'m'}
    str_nums = list()
    for divisor in (1000, 100, 10, 1):
        quotient, remainder = divmod(number, divisor)
        str_nums.append(roman_map[divisor] * quotient)
        number = remainder
    return ''.join(str_nums[::-1]).lower()
