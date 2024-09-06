
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
    tens = ['', 'x', 'xx', 'xxx', 'xl', 'xc', 'xvi', 'xvii', 'xviii', 'xix']
    hundreds = ['', 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm']
    thousands = ['','m','mm','mmm','mml','mmc','mmmm','mmmml','mmmmc']

    num_list = list(str(number))
    result = ''
    for i, j in enumerate(num_list):
        j = int(j)
        if j == 0:
            continue
        if i == 0:
            result = thousands[j] + units[j]
            continue
        if j == 1:
            result = units[j] + tens[i]
            continue
        result = tens[i] + hundreds[j]
