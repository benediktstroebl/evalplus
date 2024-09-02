
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

    # Write your code here.
    # Create a list of all roman numerals from 1 to 1000
    roman_numerals = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix',
                      'x', 'xx', 'xxx', 'l', 'lx', 'lxx', 'lxxx', 'xc', 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm',
                      'm', 'mm', 'mmm']

    return roman_numerals[number]
