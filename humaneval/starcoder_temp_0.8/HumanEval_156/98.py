
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
    result = ''
    index = 0
    while index < len(roman_numerals):
        if number >= roman_numerals[index]:
            result += roman_numerals_mini[index]
            number -= roman_numerals[index]
        else:
            index += 1
    return result

