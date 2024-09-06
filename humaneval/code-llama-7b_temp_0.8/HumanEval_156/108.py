
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
    if type(number) is not int:
        raise TypeError('number must be an integer')
    if number <= 0 or number > 1000:
        raise ValueError('number must be positive and no more than 1000')

    # use this dict to convert the numerals to the corresponding number of repetitions
    # i.e. {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numerals_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # initialize an empty string
    roman_numeral = ''

    # obtain the representation of the number in roman numerals, and the number of times it appears
    # in the numerals
    for numeral, count in numerals_dict.items():
        while number >= count:
            roman_numeral += numeral
            number -= count

    return roman_numeral

