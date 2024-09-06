
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
    roman_numbers = {
        "1000": "m",
        "900": "cm",
        "500": "d",
        "400": "cd",
        "100": "c",
        "90": "xc",
        "50": "l",
        "40": "xl",
        "10": "x",
        "9": "ix",
        "5": "v",
        "4": "iv",
        "1": "i"
    }
    roman_number = ""
    while number > 0:
        if number >= 1000:
            roman_number += "m"
            number -= 1000
        elif number >= 900:
            roman_number += "cm"
            number -= 900
        elif number >= 500:
            roman_number += "d"
            number -= 500
        elif number >= 400:
            roman_number += "cd"
            number -= 400
       
