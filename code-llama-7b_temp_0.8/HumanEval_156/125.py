
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

    digits = [
        {"name": "M", "value": 1000},
        {"name": "CM", "value": 900},
        {"name": "D", "value": 500},
        {"name": "CD", "value": 400},
        {"name": "C", "value": 100},
        {"name": "XC", "value": 90},
        {"name": "L", "value": 50},
        {"name": "XL", "value": 40},
        {"name": "X", "value": 10},
        {"name": "IX", "value": 9},
        {"name": "V", "value": 5},
        {"name": "IV", "value": 4},
        {"name": "I", "value": 1},
    ]

    roman_numeral = ""
    for digit in digits:
        while number >= digit["value"]:
            roman_numeral += digit["name"]
            number -= digit["value"]

    return roman_numeral.lower()

