
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

    if not isinstance(number, int) or number < 1 or number > 1000:
        return None
    romans = ['i', 'v', 'x', 'l', 'c', 'd']
    numerals = [1, 5, 10, 50, 100, 500]
    result = ''
    for i in range(len(romans)):
        while number >= numerals[i]:
            number -= numerals[i]
            result += romans[i]
    return result.lower()
