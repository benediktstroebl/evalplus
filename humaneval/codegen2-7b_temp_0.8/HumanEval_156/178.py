
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
    if number < 0 or number > 1000:
        return None
    elif number < 40:
        return numbers[number]
    elif number < 90:
        return numbers[10] + numbers[number % 10]
    elif number < 100:
        return numbers[100] + numbers[number % 100]
    elif number < 400:
        return numbers[1000] + numbers[number % 1000]
    elif number == 400:
        return 'cd'
    else:
        return numbers[10000
