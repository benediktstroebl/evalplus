
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
    if number <= 0:
        raise ValueError("Value must be a positive integer")

    result = ''

    for digit in str(number):
        num = int(digit)
        if num < 4:
            result += 'i' * num
        elif num == 4:
            result += 'iv'
        elif num < 9:
            result += 'v' + ('i' * (num - 5))
        elif num == 9:
            result += 'ix'

    return result

