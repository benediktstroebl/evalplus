
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
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_numbers = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    roman_values = [1, 5, 10, 50, 100, 500, 1000]
    roman_string = ''
    i = 0

    while number > 0:
        if number >= roman_values[i]:
            roman_string = roman_string + roman_dict[roman_numbers[i]] * (
                number // roman_values[i])
            number -= roman_values[i] * (number // roman_values[i])
        else:
            i += 1
    return roman_string
