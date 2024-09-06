
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
    mini_roman = {
        1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'
    }
    digit = 1
    res = []
    while number:
        digit_value = number % 10 * digit
        if digit_value < 4:
            res += [mini_roman[digit] * digit_value]
        elif digit_value == 4:
            res += [mini_roman[digit] + mini_roman[digit * 5]]
        elif digit_value < 9:
            res += [mini_roman[digit * 5] +
                    mini_roman[digit] * (digit_value - 5)]
        elif digit_value == 9:
            res += [mini_roman[digit] + mini_roman[digit * 10]]
        number //= 10
        digit *= 10
    return ''.join(res[::-1])

