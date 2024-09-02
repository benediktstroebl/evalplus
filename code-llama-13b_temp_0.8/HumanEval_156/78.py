
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
    tens = ['', 'x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc']
    ones = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    tens_result, ones_result = '', ''
    i, j = 9, 9
    while number > 0:
        if number - (10 * i) >= 0:
            tens_result = tens[i]
            number -= (10 * i)
        else:
            i -= 1
        if number - j >= 0:
            ones_result = ones[j]
            number -= j
        else:
            j -= 1
    return tens_result + ones_result
