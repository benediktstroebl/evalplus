
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

    # base case, if the number is less than 1
    if number < 1:
        return ''

    # if the number is less than 5, then there is no need to break it down further
    if number < 5:
        return number * 'i'

    # if the number is 5, return 'i'
    if number == 5:
        return 'i'

    # if the number is divisible by 5, then the number of 'i' is equal to the number divided by 5
    if number % 5 == 0:
        return (number // 5) * 'v'

    # if the number is 10, return 'x'
    if number == 10:
        return 'x'

    # if the number is divisible by 10, then the number of 'x' is equal to the number divided by 10
    if number % 10 == 0:
        return (number // 10) * 'x'

    # if the number is 50, return 'l'
    if number == 50:
        return 'l'

    # if the number is divisible by 50, then the number of 'l' is equal to the number divided by 50
    if number % 50 == 0:
        return (number // 50) * 'l'

    # if the number is 100, return 'c'
    if number == 100:
        return 'c'

    # if the number is divisible by 100, then the number of 'c' is equal to the number divided by 100
    if number % 100 == 0:
        return (number // 100) * 'c'

    # if the number is 500, return 'd'
    if number == 500:
        return 'd'

    # if the number is divisible by 500, then the number of 'd' is equal to the number divided by 500
    if number % 500 == 0:
        return (number // 500)
