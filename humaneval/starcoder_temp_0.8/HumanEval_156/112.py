
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

    # #1
    # roman = ''
    # num = number

    # while num > 0:
    #     if num >= 1000:
    #         roman += 'M'
    #         num -= 1000
    #     elif num >= 900:
    #         roman += 'CM'
    #         num -= 900
    #     elif num >= 500:
    #         roman += 'D'
    #         num -= 500
    #     elif num >= 400:
    #         roman += 'CD'
    #         num -= 400
    #     elif num >= 100:
    #         roman += 'C'
    #         num -= 100
    #     elif num >= 90:
    #         roman += 'XC'
    #         num -= 90
    #     elif num >= 50:
    #         roman += 'L'
    #         num -= 50
    #     elif num >= 40:
    #         roman += 'XL'
    #         num -= 40
    #     elif num >= 10:
    #         roman += 'X'
    #         num -= 10
    #     elif num >= 9:
    #         roman += 'IX'
    #         num -= 9
    #     elif num >= 5:
    #         roman += 'V'
    #         num -= 5
    #     elif num >= 4:
    #         roman += 'IV'
    #         num -= 4
    #     elif num >= 1:
    #         roman += 'I'
    #         num -= 1

    # #2
    # roman = ''
    # num = number

    # roman = 'M' * (num / 1000)
    # num = num % 1000
    # roman = 'D' * (num / 500) + roman
    # num = num % 500
    # roman = 'C' * (num / 100) + roman
    # num = num % 100
    # roman = 'L' * (num / 50) + roman
    # num = num % 50
    #
