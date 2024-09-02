
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
    roman = []
    while number > 0:
        if number == 1:
            roman.append('I')
        elif number == 2:
            roman.append('II')
        elif number == 3:
            roman.append('III')
        elif number == 4:
            roman.append('IV')
        elif number == 5:
            roman.append('V')
        elif number == 6:
            roman.append('VI')
        elif number == 7:
            roman.append('VII')
        elif number == 8:
            roman.append('VIII')
        elif number == 9:
            roman.append('IX')
        elif number == 10:
            roman.append('X')
        else:
            roman.append('0')
            number = number // 10

    roman.append(' ')
    return ' '.join(roman)
