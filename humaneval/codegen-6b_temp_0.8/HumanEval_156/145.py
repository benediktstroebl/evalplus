
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
    r = ""
    while number > 0:
        if number >= 1000:
            r = symbol(number % 1000) + r
            number -= 1000
        elif 100 <= number < 1000:
            r = symbol(number % 100) + r
            number -= 100
        elif 10 <= number < 100:
            r = symbol(number % 10) + r
            number -= 10
        elif number >= 1:
            r = symbol(number) + r
            number -= number
    return r
