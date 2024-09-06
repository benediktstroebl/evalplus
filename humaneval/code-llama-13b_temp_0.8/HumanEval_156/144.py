
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

    roman = ''
    while number:
        if number >= 1000:
            roman += 'm' * (number // 1000)
            number %= 1000
        elif number >= 900:
            roman += 'cm' * (number // 900)
            number %= 900
        elif number >= 500:
            roman += 'd' * (number // 500)
            number %= 500
        elif number >= 400:
            roman += 'cd' * (number // 400)
            number %= 400
        elif number >= 100:
            roman += 'c' * (number // 100)
            number %= 100
        elif number >= 90:
            roman += 'xc' * (number // 90)
            number %= 90
        elif number >= 50:
            roman += 'l' * (number // 50)
            number %= 50
        elif number >= 40:
            roman += 'xl' * (number // 40)
            number %= 40
        elif number >= 10:
            roman += 'x' * (number // 10)
            number %= 10
        elif number >= 9:
            roman += 'ix' * (number // 9)
            number %= 9
        elif number >= 5:
            roman += 'v' * (number // 5)
            number %= 5
        elif number >= 4:
            roman += 'iv' * (number // 4)
            number %= 4
        elif number >= 1:
            roman += 'i' * (number // 1)
            number %= 1
    return roman
