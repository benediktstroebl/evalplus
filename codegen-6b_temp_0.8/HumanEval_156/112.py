
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
    # WRITE YOUR CODE HERE
    i = 0
    arr = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    result = ''
    while number:
        num = number % arr[i]
        if num == 0:
            result += ' '
        elif num < 4:
            result += (num - 1) * 'i'
        elif num < 9:
            result += 'v'
        elif num == 9:
            result += 'x'
        else:
            result += 'l'
        number = number // arr[i]
        i += 1
    return result[::-1]

