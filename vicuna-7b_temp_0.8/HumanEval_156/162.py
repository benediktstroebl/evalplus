
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
    i = 0
    while number >= 10:
        number -= 10
        roman.append(str(number)[-2:])
        i += 1

    if number == 0:
        roman.append('a')
    elif number == 1:
        roman.append('i')
    elif number == 2:
        roman.append('ii')
    elif number == 3:
        roman.append('iii')
    elif number == 4:
        roman.append('iv')
    elif number == 5:
        roman.append('v')
    elif number == 6:
        roman.append('vi')
    elif number == 7:
        roman.append('vii')
    elif number == 8:
        roman.append('viii')
    elif number == 9:
        roman.append('ix')

    for i in range(i):
        roman.append(roman[i])
    return ' '.join(roman[::-1])
