
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
        return "NO ROMAN NUMERAL"
    number_string = str(number)
    mini_roman_string = ''
    for i in number_string:
        if i == '1':
            mini_roman_string += 'i'
        if i == '2':
            mini_roman_string += 'ii'
        if i == '3':
            mini_roman_string += 'iii'
        if i == '4':
            mini_roman_string += 'iv'
        if i == '5':
            mini_roman_string += 'v'
        if i == '6':
            mini_roman_string += 'vi'
        if i == '7':
            mini_roman_string += 'vii'
        if i == '8':
            mini_roman_string += 'viii'
        if i == '9':
            mini_roman_string += 'ix'
        if i == '10':
            mini_roman_string += 'x'
        if i
