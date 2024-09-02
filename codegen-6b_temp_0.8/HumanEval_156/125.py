
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
    assert 1 <= number <= 1000, 'number must be between 1 and 1000'

    romans = [
        '', 'm', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv',
        'i', 'vi', 'vii', 'viii', 'ixi', 'xix', 'x', 'xi', 'xii', 'xiii', 'xiv',
        'xv', 'xvi', 'xvii', 'xviii', 'xix', 'xc', 'cx', 'lx', 'lxi', 'lxii',
        'lxiii', 'lxiv', 'lxv', 'lxvi', 'lxvii', 'lxviii', 'lxix', 'lxx', 'lxxi',
        'lxxii', 'lxxiii', 'lxxiv', 'lxxv', 'lxxvi', 'lxxvii', 'lxxviii', 'lxxix',
        'lxxx', 'lxxxi', 'lxxxii', 'lxxxiii', 'lxxxiv', 'lxxxv', 'lxxxvi',
        'lxxxvii', 'lxxxviii', 'lxxxix', 'cx', 'cxii', 'cxiii', 'cxiv', 'cxv',
        'cxvi', 'cxvii', 'cxviii', 'cxix', 'cxx', 'cxxii', 'cxxiii', 'cxxiv',
        'cxxv', 'cxxvi', 'cxxvii', 'cxxviii', 'cxxix', 'cxxx', 'cxxxii',
        'cxxxiii', 'cxxxiv', 'cxxxv', 'cxxxvi', 'cxxxvii', 'cxxxviii', 'cxxxix',
        'd', 'dii', 'dim', 'din', 'dv', 'div', 'dvii', 'dviii', 'dix', 'dxi',
        'dxii', 'dxiii', 'dxiv', 'dxv', 'dxvi', 'dxvii', 'dx