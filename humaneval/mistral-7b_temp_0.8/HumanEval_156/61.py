
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
    conversion_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    roman_dict = {'M': 'M', 'D': 'D', 'C': 'C', 'L': 'L', 'X': 'X', 'V': 'V', 'I': 'I'}
    roman_str = ""
    while number > 0:
        for key, value in conversion_dict.items():
            if value <= number:
                roman_str += roman_dict[key]
                number -= value
                break
    return roman_str
