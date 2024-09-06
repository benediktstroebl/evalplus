
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

    if number > 1000:
        raise ValueError("Number must be between 1 and 1000, inclusive.")

    def get_num(num):
        if num == 1:
            return 'i'
        elif num == 2:
            return 'ii'
        elif num == 3:
            return 'iii'
        elif num == 4:
            return 'iv'
        elif num == 5:
            return 'v'
        elif num == 6:
            return 'vi'
        elif num == 7:
            return 'vii'
        elif num == 8:
            return 'viii'
        elif num == 9:
            return 'ix'

    while number > 0:
        if number > 1000:
            raise ValueError("Number must be between 1 and 1000, inclusive.")
        if number >= 1000:
            roman += 'm'
            number -= 1000
        elif number >= 900:
            roman += '
