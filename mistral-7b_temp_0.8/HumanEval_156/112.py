
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
    roman_num = {}
    roman_num[1000] = 'M'
    roman_num[900] = 'CM'
    roman_num[500] = 'D'
    roman_num[400] = 'CD'
    roman_num[100] = 'C'
    roman_num[90] = 'XC'
    roman_num[50] = 'L'
    roman_num[40] = 'XL'
    roman_num[10] = 'X'
    roman_num[9] = 'IX'
    roman_num[5] = 'V'
    roman_num[4] = 'IV'
    roman_num[1] = 'I'
    total = 0
    roman = ''
    for n in number:
        while number > 0:
            i = 1
            if number >= roman_num[i]:
                total += roman_num[i]
                number -= roman_num[i]
            else:
                break
    roman =
