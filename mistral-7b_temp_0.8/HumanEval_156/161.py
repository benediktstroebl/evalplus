
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
    if number == 1:
        return 'i'
    elif number == 5:
        return 'v'
    elif number == 10:
        return 'x'
    elif number == 50:
        return 'l'
    elif number == 100:
        return 'c'
    elif number == 500:
        return 'd'
    elif number == 1000:
        return 'm'
    else:
        if number % 10 == 0:
            return str(number) + int_to_mini_roman(number // 10)
        elif number % 10 == 1:
            return str(number) + int_to_mini_roman(number // 10)
        elif number % 10 == 2:
            return str(number) + int_to_mini_roman(number // 10)
        elif number % 10 == 3:
            return str(number) + int_to_mini_roman(number // 10)
       
