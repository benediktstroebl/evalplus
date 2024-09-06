
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

    # Validation
    if number <= 0:
        return "No mini-roman available for non-positive integers."
    if number > 1000:
        return "No mini-roman available for numbers > 1000."

    # Create a dictionary of miniroman letters and their corresponding values
    mini_roman_dict = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000
    }

    # Create an empty string to store the roman numeral
    rom_num = ""

    # Loop through the number and append roman numerals to the string
    while number > 0:
        for char, val in mini_roman_dict.items():
            if number >= val:
                rom_num += char
                number -= val
                break

    return rom_num

