
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
    letters = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]
    roman_num = "i"
    for i in range(2, 10):
        roman_num = roman_num + letters[i]

    letters = ["x", "xx", "xxx", "xl", "L", "LX", "LXX", "LXXX", "XC"]
    roman_num = roman_num + "x"
    for i in range(2, 10):
        roman_num = roman_num + letters[i]

    letters = ["c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm"]
    roman_num = roman_num + "c"
    for i in range(2, 10):
        roman_num = roman_num + letters[i]

    letters = ["m", "mm", "mmm"]
    roman_num = roman_num + "m"
    for i in range(
