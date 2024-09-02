
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

    # Test the inputs
    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")

    if number > 1000 or number < 1:
        raise ValueError("Number is out of range.")

    # Define the dictionary that converts to mini roman numerals
    roman_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    # Create a list of the keys (the values are irrelevant)
    keys = sorted(roman_dict, reverse=True)
    mini_roman = ''
    for key in keys:
        while number >= key:
            mini_roman += roman_dict[key]
            number -= key
    return mini_roman
