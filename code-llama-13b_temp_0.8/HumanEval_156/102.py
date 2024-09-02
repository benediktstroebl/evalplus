
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
    ones = ['i', 'x', 'c', 'm']
    fives = ['v', 'l', 'd']
    result = ""
    num = number
    if num == 0:
        return '0'
    while num > 0:
        if num < 4:
            result = ones[0] * num + result
            num = 0
        elif num == 4:
            result = ones[0] + fives[0] + result
            num = 0
        elif num < 9:
            result = fives[0] + ones[0] * (num - 5) + result
            num = 0
        elif num == 9:
            result = ones[0] + ones[1] + result
            num = 0
        elif num < 40:
            result = ones[1] * int((num - 10) / 10) + result
            num = num % 10
        elif num == 40:
            result = ones[1] + fives[1] + result
            num = 0
        elif num < 90:
            result = fives[1] + ones[1] * (num - 50) + result
            num = 0
        elif num == 90:
            result = ones[1] + ones[2] + result
            num = 0
        elif num < 400:
            result = ones[2] * int((num - 100) / 100) + result
            num = num % 100
        elif num == 400:
            result = ones[2] + fives[2] + result
            num = 0
        elif num < 900:
            result = fives[2] + ones[2] * (num - 500) + result
            num = 0
        elif num == 900:
            result = ones[2] + ones[3] + result
            num = 0
        else:
            return 'too large'
    return result.lower()

