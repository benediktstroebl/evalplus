
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

    def digit_to_mini_roman(digit):
        if digit == 1:
            return 'i'
        elif digit == 2:
            return 'ii'
        elif digit == 3:
            return 'iii'
        elif digit == 4:
            return 'iv'
        elif digit == 5:
            return 'v'
        elif digit == 6:
            return 'vi'
        elif digit == 7:
            return 'vii'
        elif digit == 8:
            return 'viii'
        elif digit == 9:
            return 'ix'

    result = ''
    while number > 0:
        digit = number % 10
        result = digit_to_mini_roman(digit) + result
        number = number // 10
    return result
