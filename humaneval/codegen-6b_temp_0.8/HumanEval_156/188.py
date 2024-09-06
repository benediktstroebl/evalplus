
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
    if number < 1 or number > 1000:
        raise ValueError

    roman_numerals = [
        {'num': 1000, 'roman': 'm'},
        {'num': 900, 'roman': 'CM'},
        {'num': 500, 'roman': 'D'},
        {'num': 400, 'roman': 'CD'},
        {'num': 100, 'roman': 'C'},
        {'num': 90, 'roman': 'XC'},
        {'num': 50, 'roman': 'L'},
        {'num': 40, 'roman': 'XL'},
        {'num': 10, 'roman': 'X'},
        {'num': 9, 'roman': 'IX'},
        {'num': 5, 'roman': 'V'},
        {'num': 4, 'roman': 'IV'},
        {'num': 1, 'roman': 'I'}
    ]

    return ''.join([
        partial_roman(number - roman_numerals[i - 1]['num']).lower()
        for i, roman in enumerate(roman_numerals, start=1)
    ])

