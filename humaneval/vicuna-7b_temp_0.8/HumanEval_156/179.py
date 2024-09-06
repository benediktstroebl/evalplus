
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
    roman_map = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_number = str(number)

    # Convert the number to Roman numeral
    roman_number_index = 0
    while roman_number[roman_number_index] in ['M', 'D', 'C', 'L', 'X', 'V', 'I']:
        roman_number_index += 1
    roman_number = roman_number[:roman_number_index]

    # Create the resulting string
    result_str = ''
    for char in roman_number:
        if char.isalpha():
            result_str += chr(ord(char) - 70)
        else:
            result_str += chr(ord(char) + 13)
    result_str = result_str[::-1]
    return result_str.lower()
