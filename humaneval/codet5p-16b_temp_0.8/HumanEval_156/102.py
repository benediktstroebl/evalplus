
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

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    roman = ''
    for i in range(len(str(number))):
        if number >= 1000:
            roman += roman_dict[str(1000)]
            number -= 1000
            continue

        if number >= 900:
            roman += roman_dict[str(900)]
            number -= 900
            continue

        if number >= 500:
            roman += roman_dict[str(500)]
            number -= 500
            continue

        if number >= 400:
            roman += roman_dict[str(400)]
            number -= 400
            continue

        if number >= 100:
            roman += roman_dict[str(100)]
            number -= 100
            continue

        if number >= 90:
            roman += roman_dict[str(90)]
            number -= 90
            continue

        if number >= 50:
            roman += roman_dict[str(50)]
            number -= 50
            continue
