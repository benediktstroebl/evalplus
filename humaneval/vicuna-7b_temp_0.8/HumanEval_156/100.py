
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
    roman = ''
    for i in range(1000):
        if number >= (i * 1000):
            roman += str(i)
            number -= (i * 1000)
        elif number >= (i * 100):
            roman += str(i)
            number -= (i * 100)
        elif number >= (i * 10):
            roman += str(i)
            number -= (i * 10)
        else:
            roman += str(i)
            number -= (i * 10)
    return roman.lower()
