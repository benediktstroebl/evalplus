
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
    romans = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
    if number < 0 or number > 1000:
        raise ValueError("Input must be a positive integer between 1 and 1000")
    return ''.join(romans[(number - 1) // 100] + romans[(number - 1) % 100 // 10] +
                   romans[(number - 1) % 10
