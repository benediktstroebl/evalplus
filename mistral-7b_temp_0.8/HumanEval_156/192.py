
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
    roman_n_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    roman_s_dict = {
        'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'
    }

    roman_str = ''
    while number > 0:
        div_quot, mod = divmod(number, 10)
        div_quot, mod = divmod(div_quot, 10)
        div_quot, mod = divmod(div_quot, 10)

        if div_quot > 0:
            roman_str += roman_s_dict[roman_n_dict[roman_str[-1]]] * div_quot

        if div_quot == 0 and mod > 0
