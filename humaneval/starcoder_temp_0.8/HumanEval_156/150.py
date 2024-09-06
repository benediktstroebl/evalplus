
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

    # there are 7 cases
    if number >= 1000:
        return 'M' + int_to_mini_roman(number-1000)
    elif number >= 900:
        return 'CM' + int_to_mini_roman(number-900)
    elif number >= 500:
        return 'D' + int_to_mini_roman(number-500)
    elif number >= 400:
        return 'CD' + int_to_mini_roman(number-400)
    elif number >= 100:
        return 'C' + int_to_mini_roman(number-100)
    elif number >= 90:
        return 'XC' + int_to_mini_roman(number-90)
    elif number >= 50:
        return 'L' + int_to_mini_roman(number-50)
    elif number >= 40:
        return 'XL' + int_to_mini_roman(number-40)
    elif number >= 10:
        return 'X' + int_to_mini_roman(number-10)
    elif number >= 9:
        return 'IX' + int_to_mini_roman(number-9)
    elif number >= 5:
        return 'V' + int_to_mini_roman(number-5)
    elif number >= 4:
        return 'IV' + int_to_mini_roman(number-4)
    elif number >= 1:
        return 'I' + int_to_mini_roman(number-1)
    elif number == 0:
        return ''
