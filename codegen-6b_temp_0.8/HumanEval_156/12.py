
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
    roman_numeral_dict = {1 : 'i', 2 : 'ii', 3 : 'iii', 4 : 'iv', 5 : 'v',
                          6 : 'vi', 7 : 'vii', 8 : 'viii', 9 : 'ix',
                          10 : 'x', 11 : 'xi', 12 : 'xii',
                          13 : 'xiii', 14 : 'xiv', 15 : 'xix', 16 : 'x',
                          17 : 'xix', 18 : 'x', 19 : 'ix', 20 : 'x',
                          30 : 'xc', 40 : 'cd', 50 : 'd', 60 : 'dc',
                          70 : 'dcc', 80 : 'dccc', 90 : 'dcccc',
                          100 : 'c', 200 : 'cc', 300 : 'ccc', 400 : 'cccc',
                          500 : 'cd', 600 : 'cdc', 700 : 'cdcc', 800 : 'cdccc',
                          900 : 'cdcccc'}

    # Fill the roman numeral list from the front of the number to the end.
    # Make sure that all characters are lowercase.
    roman_numeral_list = []
    for val in range(number // 10 * 10, number, 10):
        roman_numeral_list.append(roman_numeral_dict[val])

    # Fill the list from the back of the number to the front, adjusting the
    # numerals for each fact they occur.
    for val in range(number // 10, 0, -10):
        if roman_numeral_list[val - 1] == 'x':
            roman_numeral_list[val] = roman_numeral_list[val - 1] + roman_numeral_list[val]
            roman_numeral_list[val - 1] = roman_numeral_dict[val - 10]
    # Fill the list from the back of the number to the front, except
    # for the last character, which is added on to the front.
    for val in range(number % 10, 0, -10):
        roman_numeral_list.insert(0, roman_numeral_dict[val])

    return ''.join(roman