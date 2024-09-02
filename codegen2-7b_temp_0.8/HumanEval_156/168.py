
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
    if number < 1:
        raise ValueError
    if number > 1000:
        raise ValueError
    return ''.join(
        (chr(0x4E00 + number % 10), chr(0x4E00 + number % 10)) if (number % 10) > 0 else
        (chr(0x4E00 + number % 10), '')
        for number in range(number // 10))
