
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
        return None
    for i in range(number):
        if i == 0:
            result += 'i'
        elif i == 1:
            result += 'vi'
        elif i == 2:
            result += 'xi'
        elif i == 3:
            result += 'xv'
        elif i == 4:
            result += 'l'
    return result.lower()

