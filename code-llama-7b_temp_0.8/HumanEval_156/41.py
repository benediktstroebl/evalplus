
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
    # Base cases
    if number <= 0:
        return ''
    elif number <= 3:
        return 'iii' * number
    elif number <= 5:
        return 'v' + 'iii' * (number - 5)
    elif number <= 8:
        return 'viii' + 'iii' * (number - 8)
    elif number <= 10:
        return 'x' + 'iii' * (number - 10)

    if number < 40:
        return 'x' * (number // 10) + 'iii' * (number % 10)
    elif number < 50:
        return 'x' * (10 - number // 10) + 'v' + 'iii' * (number % 10)
    elif number < 90:
        return 'x' * (number // 10 - 5) + 'viii' + 'iii' * (number % 10)
    else:
        return 'x' * (number // 10 - 10) + 'x' + 'iii' * (number % 10)

