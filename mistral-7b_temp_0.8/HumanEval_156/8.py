
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
    number_to_roman = {1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v', 6: 'vi',
                       7: 'vii', 8: 'viii', 9: 'ix', 10: 'x',
                       20: 'xx', 30: 'xxx', 40: 'xl', 50: 'l', 60: 'lx',
                       70: 'lxx', 80: 'lxx', 90: 'xc', 100: 'c'}
    roman_numbers = []
    while number > 0:
        if number in number_to_roman:
            roman_numbers.append(number_to_roman[number])
            number = 0
        else:
            roman_numbers.append(number_to_roman[number // 10])
            number = number - (number // 10) * 10

    roman_numbers.reverse()
    return ''.join(
