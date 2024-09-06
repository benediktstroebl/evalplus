
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
    if number > 3000 or number < 1:
        return None

    number_roman = []
    while number > 0:
        if number >= 1000:
            number_roman.append("M")
            number -= 1000
        elif number >= 900:
            number_roman.append("CM")
            number -= 900
        elif number >= 500:
            number_roman.append("D")
            number -= 500
        elif number >= 400:
            number_roman.append("CD")
            number -= 400
        elif number >= 100:
            number_roman.append("C")
            number -= 100
        elif number >= 90:
            number_roman.append("XC")
            number -= 90
        elif number >= 50:
            number_roman.append("L")
            number -= 50
        elif number >= 40:
            number_roman.append("XL")
            number -= 40
        elif number >= 10:
            number_roman.append("X")
            number -= 10
        elif number >= 9:
            number_roman.append("IX")
            number -= 9
        elif number >= 5:
            number_roman.append("V")
            number -= 5
        elif number >= 4:
            number_roman.append("IV")
            number -= 4
        elif number >= 1:
            number_roman.append("I")
            number -= 1

    return ''.join(number_roman)

