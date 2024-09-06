
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
    numeral_string = ""
    if number < 0:
        raise ValueError('Numbers must be positive')
    elif number > 1000:
        raise ValueError('Numbers must be less than 1000')
    else:
        roman = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numeral = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
        for i in range(len(roman)):
            while number >= roman[i]:
                number -= roman[i]
                numeral_string += numeral[i]
    return numeral_string

