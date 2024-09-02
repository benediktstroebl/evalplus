
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
    roman = ''
    number = str(number)
    if number == '0':
        return '0'
    for i in range(0, len(number)):
        if number[i] == '1':
            roman += 'i'
        elif number[i] == '2':
            roman += 'ii'
        elif number[i] == '3':
            roman += 'iii'
        elif number[i] == '4':
            roman += 'iv'
        elif number[i] == '5':
            roman += 'v'
        elif number[i] == '6':
            roman += 'vi'
        elif number[i] == '7':
            roman += 'vii'
        elif number[i] == '8':
            roman += 'viii'
        elif number[i] == '9':
            roman += 'ix'
        elif number[i] == '0':
            roman += 'x'
    return roman

