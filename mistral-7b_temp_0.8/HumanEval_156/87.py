
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

    roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    roman_dict = dict((k,v) for k,v in roman_dict.items() if v < 1000)
    roman_dict[0] = 0
    roman_num = ""
    for roman_char,int_value in roman_dict.items():
        while number >= int_value:
            number -= int_value
            roman_num += roman_char
    return roman_num
