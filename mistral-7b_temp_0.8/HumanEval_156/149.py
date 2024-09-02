
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
    assert number > 0 and number <= 1000, 'number must be in range 1-1000'

    digits = ['i', 'v', 'x', 'l', 'c', 'd', 'm']
    powers = [1, 5, 10, 50, 100, 500, 1000]
    roman = ''

    for i in range(len(powers)):
        while number >= powers[i]:
            roman += digits[i]
            number -= powers[i]

    return roman
