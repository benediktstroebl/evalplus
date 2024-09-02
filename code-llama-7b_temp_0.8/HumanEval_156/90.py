
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
    # A list of all roman numerals and their value in base 10
    num_dict = {
        'm': 1000,
        'd': 500,
        'c': 100,
        'l': 50,
        'x': 10,
        'v': 5,
        'i': 1
    }
    roman_string = ''
    for letter, value in num_dict.items():
        # Use a while loop to get each roman numeral
        # for each letter in the dictionary
        while number > 0:
            if number - 3 * value >= 0:
                # Three of this letter
                roman_string += letter * 3
                number -= value * 3
            elif number - value >= 0:
                # One of this letter
                roman_string += letter
                number -= value
                break
            else:
                # No more of this letter
                break
    return roman_string.lower()

