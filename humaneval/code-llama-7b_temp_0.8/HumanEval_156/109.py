
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

    # Use a dictionary to hold the integer-to-roman conversion
    # NOTE: This could be a constant, but we're demonstrating a mutable
    # data structure here.
    conv_dict = {1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x',
                 40: 'xl', 50: 'l', 90: 'xc', 100: 'c',
                 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}

    roman = ""

    # Repeatedly divide by 1000 and append the corresponding roman
    # numeral to the result. Keep track of any remainder that is
    # less than 1000 and repeat the process until it is equal to 0.
    while number > 0:
        if number >= 1000:
            roman += conv_dict[1000]
            number -= 1000
        elif number >= 900:
            roman += conv_dict[900]
            number -= 900
        elif number >= 500:
            roman += conv_dict[500]
            number -= 500
        elif number >= 400:
            roman += conv_dict[400]
            number -= 400
        elif number >= 100:
            roman += conv_dict[100]
            number -= 100
        elif number >= 90:
            roman += conv_dict[90]
            number -= 90
        elif number >= 50:
            roman += conv_dict[50]
            number -= 50
        elif number >= 40:
            roman += conv_dict[40]
            number -= 40
        elif number >= 10:
            roman += conv_dict[10]
            number -= 10
        elif number >= 9:
            roman += conv_dict[9]
            number -= 9
        elif number >= 5:
