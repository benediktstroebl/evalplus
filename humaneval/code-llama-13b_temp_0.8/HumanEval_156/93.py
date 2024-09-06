
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

    num_to_str = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }
    int_to_roman = {
        1: ('', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix'),
        5: ('', 'v', 'x'),
        10: ('', 'x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc'),
        50: ('', 'l', 'lv', 'lx', 'lxx', 'lxxx', 'xc'),
        100: ('', 'c', 'ci', 'cii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix'),
        500: ('', 'd', 'di', 'dii', 'diii', 'div', 'v', 'vi', 'vii', 'viii', 'ix'),
        1000: ('', 'm', 'mi', 'mii', 'miii', 'miv', 'v', 'vi', 'vii', 'viii', 'ix'),
    }

    s = ''
    for num in sorted(num_to_str.keys(), reverse=True):
        while number >= num:
            s += num_to_str[num]
            number -= num

    s = s.replace('iv', 'iiii').replace('ix', 'viii')
    s = s.replace('xl', 'lxxxx').replace('xc', 'xxxxv')
    s = s.replace('cd', 'dcccc').replace('cm', 'mmmmc')
    s = s.replace('miv', 'mmv').replace('mxi', 'mmxi')

    for num in sorted(int_to_roman.keys(), reverse=True):
        s = s.replace(int_to_roman[num][0], num_to_str[num])
