
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
    map_symb = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    symb_str = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    symb_to_subtract = ['M', 'C', 'X', 'V']
    res = ""
    for symb in symb_str:
        if number == map_symb[symb]:
            res += symb
            break
        elif number < map_symb[symb]:
            res += symb
            number -= map_symb[symb]

    while True:
        for i in range(1, 3):
            if number < map_symb[symb_str[i]]:
                if symb_str[i] in symb_to_subtract:
                    res += symb_str[i]
                else:
                    res += symb
