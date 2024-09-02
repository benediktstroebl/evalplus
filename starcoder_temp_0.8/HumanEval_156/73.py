
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
    x = 0
    while number:
        if number - 1000 >= 0:
            roman += 'M' * (number // 1000)
            number -= 1000 * (number // 1000)
        elif number - 900 >= 0:
            roman += 'CM' * (number // 900)
            number -= 900 * (number // 900)
        elif number - 500 >= 0:
            roman += 'D' * (number // 500)
            number -= 500 * (number // 500)
        elif number - 400 >= 0:
            roman += 'CD' * (number // 400)
            number -= 400 * (number // 400)
        elif number - 100 >= 0:
            roman += 'C' * (number // 100)
            number -= 100 * (number // 100)
        elif number - 90 >= 0:
            roman += 'XC' * (number // 90)
            number -= 90 * (number // 90)
        elif number - 50 >= 0:
            roman += 'L' * (number // 50)
            number -= 50 * (number // 50)
        elif number - 40 >= 0:
            roman += 'XL' * (number // 40)
            number -= 40 * (number // 40)
        elif number - 10 >= 0:
            roman += 'X' * (number // 10)
            number -= 10 * (number // 10)
        elif number - 9 >= 0:
            roman += 'IX' * (number // 9)
            number -= 9 * (number // 9)
        elif number - 5 >= 0:
            roman += 'V' * (number // 5)
            number -= 5 * (number // 5)
        elif number - 4 >= 0:
            roman += 'IV' * (number // 4)
            number -= 4 * (number // 4)
        elif number - 1
