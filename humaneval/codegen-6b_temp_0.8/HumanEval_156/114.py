
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
    assert type(number) == int, 'number must be an integer'
    assert 1 <= number <= 1000, 'number must be a positive integer'

    if number < 40:
        return int_to_roman(number)

    roman_numerals = ['c', 'x', 'i', 'v', 'l', 'x', 'x', 'i', 'i', 'i', 'v',
                      'v', 'i', 'x', 'c', 'c', 'c', 'v', 'l', 'l', 'l', 'l',
                      'v', 'v', 'i', 'v', 'i', 'v', 'v', 'i']

    min_numerals = ['', '', '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '