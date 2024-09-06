
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
    if number <= 0 or number > 1000:
        raise ValueError("Number must be between 1 and 1000")

    roman_numerals_list = []
    for i in range(1, number + 1):
        if i == 1:
            roman_numerals_list.append('i')
        elif i == 2:
            roman_numerals_list.append('ii')
        elif i == 3:
            roman_numerals_list.append('iii')
        elif i == 4:
            roman_numerals_list.append('iv')
        elif i == 5:
            roman_numerals_list.append('v')
        elif i == 6:
            roman_numerals_list.append('vi')
        elif i == 7:
            roman_numerals_list.append('vii')
        elif i == 8:
            roman_numerals_list.append('viii')
        elif i == 9:
            roman_numerals_list.append('ix')
        elif i == 10:
            roman_numerals_list.append('x')
        elif i == 11:
            roman_numerals_list.append('xi')
        elif i == 12:
            roman_numerals_list.append('xii')
        elif i == 13:
            roman_numerals_list.append('xiii')
        elif i == 14:
            roman_numerals_list.append('xiv')
        elif i == 15:
            roman_numerals_list.append('xv')
        elif i == 16:
            roman_numerals_list.append('xvi')
        elif i == 17:
            roman_numerals_list.append('xvii')
        elif i == 18:
            roman_numerals_list.append('xviii')
        elif i == 19:
            roman_numerals_list.append('xix')
        elif i == 20:
            roman_numerals_list.append('xx')
        elif i == 30:
            roman_n