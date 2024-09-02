
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
    if number >= 1000:
        return 'm' * (number // 1000) + int_to_mini_roman(number % 1000)
    elif number >= 900:
        return 'cm' + int_to_mini_roman(number % 100)
    elif number >= 500:
        return 'd' + int_to_mini_roman(number % 100)
    elif number >= 400:
        return 'cd' + int_to_mini_roman(number % 100)
    elif number >= 100:
        return 'c' + int_to_mini_roman(number % 100)
    elif number >= 90:
        return 'xc' + int_to_mini_roman(number % 10)
    elif number >= 50:
        return 'l' + int_to_mini_roman(number % 10)
    elif number >= 40:
       
