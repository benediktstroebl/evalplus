
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
    # BEGIN int_to_mini_roman
    if number<1 or number>1000:
        raise ValueError
    roman_numeral = ''
    roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    i = 0
    while number > 0:
        div, mod = divmod(number, roman_values[i])
        number -= div
        if div==9:
            roman_numeral += 'ix'
        elif div==4:
            roman_numeral += 'iv'
        elif div==3:
            roman_numeral += 'ix'
        elif div==5:
            roman_numeral += 'v'
        elif div==2:
            roman_numeral += 'ii'
        elif div==1:
            roman_numeral += 'i'
        elif div==8:
            roman_numeral += 'vii'
        elif div==7:
            roman_numeral += 'v'
        elif div==6:
            roman_numeral += 'vi'
        elif div==9:
            roman_numeral += 'ix'
        elif div==4:
            roman_numeral += 'iv'
        elif div==3:
            roman_numeral += 'ix'
        elif div==1:
            roman_numeral += 'i'
        else:
            pass
        i += 1
    return roman_numeral.lower()
    # END int_to_mini_roman

