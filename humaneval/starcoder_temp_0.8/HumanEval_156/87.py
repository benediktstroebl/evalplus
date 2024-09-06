
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
    def get_n_list(n, list_of_roman):
        if n in list_of_roman:
            return list_of_roman.index(n)
        else:
            return get_n_list(n - 1, list_of_roman)

    list_of_roman = ['i', 'v', 'x', 'l', 'c','m']
    roman_numeral = ''
    n = 0
    while n!= number:
        #if number >= 9:
            #if number - 9 in list_of_roman:
                #roman_numeral = 'x' + list_of_roman[number - 9]
            #else:
                #roman_numeral = 'x' + list_of_roman[get_n_list(number - 9, list_of_roman)]
        if number >= 4:
            if number - 4 in list_of_roman:
                roman_numeral = 'iv'
            else:
                roman_numeral = 'iv' + list_of_roman[get_n_list(number - 4, list_of_roman)]
        if number >= 5:
            if number - 5 in list_of_roman:
                roman_numeral = 'v' + list_of_roman[number - 5]
            else:
                roman_numeral = 'v' + list_of_roman[get_n_list(number - 5, list_of_roman)]
        if number >= 10:
            if number - 10 in list_of_roman:
                roman_numeral = 'x' + list_of_roman[number - 10]
            else:
                roman_numeral = 'x' + list_of_roman[get_n_list(number - 10, list_of_roman)]
        if number >= 40:
            if number - 40 in list_of_roman:
                roman_numeral = 'xl'
            else:
                roman_numeral = 'xl' + list_of_roman[get_n_list(number - 40, list_of_roman)]
        if number >= 50:
            if number - 50 in list_of_roman:
                roman_numeral
