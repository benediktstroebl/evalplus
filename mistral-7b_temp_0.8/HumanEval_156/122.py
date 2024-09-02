
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
    letters = 'imcmcvxdl'
    digits = [1000, 500, 100, 50, 10, 5, 1]
    roman_letters = ['m', 'd', 'c', 'l', 'x', 'v', 'i']
    result = ''
    for i in range(len(digits)):
        while number >= digits[i]:
            result += roman_letters[i]
            number -= digits[i]
    return result

