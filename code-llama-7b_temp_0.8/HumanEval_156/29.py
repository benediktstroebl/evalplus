
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
    # Define dictionary to assist in converting between roman and arabic numerals
    roman_nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Initialize result to empty string
    result = ''

    # Loop through the roman numeral dictionary in ascending order of value
    for letter, value in sorted(roman_nums.items(), key=lambda x: x[1]):
        # Replace the number of times the roman numeral occurs with a single letter
        number = number // value
        result += letter * number
        # Subtract the number of times the roman numeral occurs from the original number
        number %= value

    return result
