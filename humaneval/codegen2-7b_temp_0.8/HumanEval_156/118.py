
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
    assert 1 <= number <= 1000
    ones = ["", "i", "ii", "iii", "iv", "v", "vi", "vii"]
    tens = ["", "x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc", "c", "cx", "cxx", "cxxx"]
    return ''.join(tens[(number / 100)] + ones[(number % 100
