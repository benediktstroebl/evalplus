
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
    result = ''
    if number > 1000 or number < 1:
        raise ValueError
    elif number >= 100:
        result += chr(number//100 + 0x30)
        number %= 100
    if number >= 10:
        result += chr(number//10 + 0x30)
        number %= 10
    if number > 0:
        result += chr(number + 0x30)
    return result.lower
