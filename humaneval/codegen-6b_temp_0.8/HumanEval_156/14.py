
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
    numerals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = []
    for i, numeral in enumerate(numerals):
        if not (1 <= number - numeral < numeral):
            raise ValueError('{} is not a valid number'.format(number))
        result.append(numeral * (number // numeral))
        number %= numeral
    return ''.join(reversed(result))

