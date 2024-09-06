
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
    units = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    tens = ['', 'x', 'xx', 'xxx', 'l']
    hundreds = ['', 'c', 'cc', 'ccc', 'd']
    thousands = ['', 'm']

    roman = thousands[number // 1000] + hundreds[number // 100 % 10] \
            + tens[number // 10 % 10] + units[number % 10]

    return roman.lower()

