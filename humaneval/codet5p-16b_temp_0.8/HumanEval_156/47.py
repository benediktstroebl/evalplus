
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

    roman_dict = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M',
    }
    mini_roman_numeral = ''
    for i in range(1, number + 1):
        if i in roman_dict:
            mini_roman_numeral += roman_dict[i]
        elif i == 4:
            mini_roman_numeral += roman_dict[5] + roman_dict[1]
        elif i == 9:
            mini_roman_numeral += roman_dict[10] + roman_dict[1]
        else:
            if i < 4:
                mini_roman_numeral += roman_dict[i * 5]
            elif i == 4:
                mini_roman_numeral += roman_dict[1] + roman_dict[5]
            elif i < 9:
                mini_roman_numeral += roman_dict[5]
