
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
    if number < 1 or number > 1000:
        raise Exception("Number out of range")
    roman = 'I'
    for i in range(2, 10):
        if i % 2 == 0:
            roman += 'V'
        else:
            roman += 'L'
    for i in range(4, 9):
        roman += 'C'
    for i in range(6, 9):
        roman += 'D'
    for i in range(4, 9):
        roman += 'M'
    return roman

