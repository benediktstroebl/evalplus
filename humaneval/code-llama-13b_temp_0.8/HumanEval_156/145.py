
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
    # The list of roman numerals in descending order by value
    roman_numerals = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

    # A dictionary that maps roman numerals to their integer values
    roman_numeral_to_value = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    def _convert_to_roman(number):
        result = ''
        for roman_numeral in roman_numerals:
            while number >= roman_numeral_to_value[roman_numeral]:
                number -= roman_numeral_to_value[roman_numeral]
                result += roman_numeral
        return result

    return _convert_to_roman(number)

