
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
    # if number < 1 or number > 1000:
    #     return ''

    digits_dict = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
    }
    roman_list = []
    while number > 0:
        for roman, value in digits_dict.items():
            if number - value >= 0:
                number -= value
                roman_list.append(roman)
                break
    return ''.join(roman_list).lower()

