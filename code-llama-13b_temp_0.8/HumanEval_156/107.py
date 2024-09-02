
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

    result = ''

    while number != 0:
        cur_digit = number % 10
        number = number // 10

        if cur_digit == 0:
            continue

        if cur_digit == 4 or cur_digit == 9:
            result += fives[number % 5 - 1]
            number = number // 5
            if number == 0:
                continue

        if cur_digit == 5:
            result += fives[number % 5 - 1]
            number = number // 5
            continue

        if cur_digit == 1:
            result += ones[number % 5 - 1]
            number = number // 5
            continue

        if cur_digit == 2 or cur_digit == 3:
            result += ones[number % 5 - 1] * (cur_digit - 1)
            number = number // 5
            continue

        if cur_digit == 8 or cur_digit == 7:
            result += ones[number % 5 - 1]
            result += fives[number % 5 - 1]
            number = number // 5
            continue

        if cur_digit == 6:
            result += fives[number % 5 - 1]
            result += ones[number % 5 - 1]
            number = number // 5
            continue

    return result[::-1]

