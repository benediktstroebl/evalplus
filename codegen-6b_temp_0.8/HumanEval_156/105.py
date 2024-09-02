
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
    if number < 1 or number > 1000:
        return None
    roman_numeral = ''
    # sum is the value of the next bigger number (which is the current number + 1)
    while number > 0:
        # if the next bigger number is in the range of 1 to 5, add it to the roman numeral
        if (number-1) % 10 == 1:
            roman_numeral = 'i' + roman_numeral
        # if the next bigger number is in the range of 2 to 10, add it to the roman numeral
        elif (number-1) % 10 == 2:
            roman_numeral = 'ii' + roman_numeral
        # if the next bigger number is in the range of 3 to 50, add it to the roman numeral
        elif (number-1) % 10 == 3:
            roman_numeral = 'iii' + roman_numeral
        # if the next bigger number is in the range of 4 to 100, add it to the roman numeral
        elif (number-1) % 10 == 4:
            roman_numeral = 'iv' + roman_numeral
        # if the next bigger number is in the range of 5 to 500, add it to the roman numeral
        elif (number-1) % 10 == 5:
            roman_numeral = 'v' + roman_numeral
        # if the next bigger number is in the range of 6 to 50, add it to the roman numeral
        elif (number-1) % 10 == 6:
            roman_numeral = 'vi' + roman_numeral
        # if the next bigger number is in the range of 7 to 50, add it to the roman numeral
        elif (number-1) % 10 == 7:
            roman_numeral = 'vii' + roman_numeral
        # if the next bigger number is in the range of 8 to 50, add it to the roman numeral
        elif (number-1) % 10 == 8:
            roman_numeral = 'viii' + roman_numeral
        # if the next bigger number is in the range of 9 to 50, add it to the