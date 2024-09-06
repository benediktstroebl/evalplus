
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
    int_to_roman = { 1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L',
                    90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M' }
    roman_string = ''
    while number != 0:
        for key in sorted(int_to_roman.keys(), reverse=True):
            if number - key >= 0:
                roman_string += int_to_roman[key]
                number -= key
                break
    return roman_string.lower()
