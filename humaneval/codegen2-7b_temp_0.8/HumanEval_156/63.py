
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
    result = ""
    for roman_number in range(1, 11):
        number_of_times = number // roman_number
        if number_of_times:
            result += roman_number * int_to_mini_roman(number_of_times)
            number -= number_of_times * roman_number
    result += chr(number + ord('a'))
    return result.lower()
