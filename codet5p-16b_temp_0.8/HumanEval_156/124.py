
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

    list_of_numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    list_of_roman_numbers = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman_number = ''

    for i in range(len(list_of_numbers)):
        while number >= list_of_numbers[i]:
            roman_number += list_of_roman_numbers[i]
            number -= list_of_numbers[i]
    return roman_number.lower()
