
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

    if not 1 <= number <= 1000:
        raise ValueError('Invalid Input')

    roman_numerals = ['i', 'v', 'x', 'l', 'c', 'd','m']
    result = ''
    while number > 0:
        for i in range(0, len(roman_numerals)):
            roman_numerals[i] *= number
            if sum(roman_numerals) >= number:
                result += roman_numerals[i]
                number -= roman_numerals[i]
                break

    return result.lower()

