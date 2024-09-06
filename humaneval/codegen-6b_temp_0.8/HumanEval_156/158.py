
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
    r_val = ''

    if number < 1000:

        ones = number // 1 % 10
        tens = number // 10 % 10
        hundreds = number // 100 % 10

        roman_dict = {1: 'I',
                      5: 'V',
                      10: 'X',
                      50: 'L',
                      100: 'C',
                      500: 'D',
                      1000: 'M'}

        r_val = roman_dict[ones] + r_val
        r_val = roman_dict[tens * 10] + r_val
        r_val = roman_dict[hundreds * 100] + r_val

        if number % 100 == 0:
            r_val = roman_dict[100] + r_val

    return r_val.lower()
