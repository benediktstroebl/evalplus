
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
    numerals = {'1': 'x', '2': 'li', '3': 'iii', '4': 'iv', '5': 'v',
                '6': 'vi', '7': 'vii', '8': 'viii', '9': 'ix', '10': 'x',
                '20': 'x', '30': 'x', '40': 'x', '50': 'x', '60': 'x',
                '70': 'x', '80': 'x', '90': 'x', '100': 'c', '200': 'c',
                '300': 'cc', '400': 'cd', '500': 'd', '600': 'cm', '700': 'c',
                '800': 'c', '900': 'm', '1000': '', '2000': '', '3000': '',
                '4000': '', '5000': '', '6000': '', '7000': '', '8000': '',
                '9000': '', '10000': '', '20000': '', '30000': '', '40000': ''}
    result = ''
    if 0 < number < 4000:
        while number > 0:
            mod = number % 10
            if mod > 0:
                if mod < 5:
                    result += numerals[str(mod)]
                elif mod == 5:
                    if mod == 5:
                        result += numerals[str(mod)] + numerals[str(mod - 5)]
                    else:
                        result += numerals[str(mod)] + numerals[str(mod - 5)] + 'i'
                else:
                    result += numerals[str(mod)] + numerals[str(mod - 5)] + 'vi'
            number //= 10
        return result[::-1]
    return ''

