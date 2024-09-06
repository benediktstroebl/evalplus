
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
    if number <= 0:
        return ''
    if number <= 10:
        # single characters
        return [v for k, v in MINI_ROMAN_NUMERALS.items() if k == number][0]
        # all the other cases
    elif number <= 50:
        # first half
        return ''.join([MINI_ROMAN_NUMERALS[10 + i] for i in range(number - 10)])
    elif number <= 100:
        # second half
        return ''.join([MINI_ROMAN_NUMERALS[50 + i] for i in range(number - 50)])
    elif number <= 500:
        # first and second halves
        return ''.join([MINI_ROMAN_NUMERALS[100 + i] for i in range(number - 100)])
    else:
        return ''.join([MINI_ROMAN_NUMERALS[100 + i] for i in range(number - 1000)])

