
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
    if not isinstance(number, int):
        raise TypeError('number must be an integer')
    if number < 1 or number > 1000:
        raise ValueError('number must be between 1 and 1000')

    digits = ['i', 'x', 'c','m']
    return ''.join(digits[number / 1000] + digits[number % 1000 // 100] + digits[number % 100 // 10] + digits[number % 10])

