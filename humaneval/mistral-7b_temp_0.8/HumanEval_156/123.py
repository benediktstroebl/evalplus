
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
    mini_roman = {}
    mini_roman['I'] = 1
    mini_roman['V'] = 5
    mini_roman['X'] = 10
    mini_roman['L'] = 50
    mini_roman['C'] = 100
    mini_roman['D'] = 500
    mini_roman['M'] = 1000

    roman = []
    while number > 0:
        if number < mini_roman['I']:
            return 'Invalid number'

        if number >= mini_roman['M']:
            roman.append('M')
            number = number - mini_roman['M']
        elif number >= mini_roman['D']:
            roman.append('D')
            number = number - mini_roman['D']
        elif number >= mini_roman['C']:
            roman.append('C')
            number = number - mini_roman['C']
        elif number >= mini_roman['L']:
            roman.append('
