
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
        raise ValueError('number out of bounds!')
    roman = []
    roman_dict = {1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c',
                  90: 'xc', 50: 'l', 40: 'xl', 10: 'x', 9: 'ix', 5: 'v',
                  4: 'iv', 1: 'i'}
    while number > 0:
        for key, value in roman_dict.items():
            if number >= key:
                roman.append(value)
                number -= key
                break
    roman.reverse()
    return ''.join(roman)

