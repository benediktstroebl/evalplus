
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
    thousands = ''.join(['M' for _ in range(number // 1000)])
    hundreds = ''.join(['C' for _ in range(number // 100)])
    tens = ''.join(['X' for _ in range(number // 10)])
    ones = ''.join(['I' for _ in range(number % 10)])
    result =  thousands + hundreds + tens + ones
    if number < 0:
        raise ValueError('Input value must be greater than zero!')
    return result
