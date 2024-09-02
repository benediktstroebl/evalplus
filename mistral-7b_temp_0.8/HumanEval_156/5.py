
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
    if number < 1:
        raise ValueError('Must be positive')
    mini_roman = ''
    while number:
        number, rest = divmod(number, 10)
        if rest >= 9:
            mini_roman += 'CM'
        elif rest >= 5:
            mini_roman += 'D'
        elif rest >= 4:
            mini_roman += 'CD'
        elif rest == 3:
            mini_roman += 'C'
        elif rest >= 2:
            mini_roman += 'L'
        elif rest >= 1:
            mini_roman += 'X'
        elif rest == 0:
            mini_roman += 'I'
    return mini_roman

