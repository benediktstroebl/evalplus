
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

    if 0 < number < 4000:
        if number == 4:
            return 'iv'
        elif number == 9:
            return 'ix'
        elif number == 40:
            return 'xl'
        elif number == 90:
            return 'xc'
        elif number == 400:
            return 'cd'
        elif number == 900:
            return 'cm'
        else:
            if number >= 500:
                return int_to_mini_roman(int(number / 100)) + 'd' + int_to_mini_roman(number % 100)
            elif number >= 100:
                return int_to_mini_roman(int(number / 100)) + 'c' + int_to_mini_roman(number % 100)
            elif number >= 50:
                return int_to_mini_roman(int(number / 10)) + 'l' + int_to_mini_roman(number % 10)
            elif number >= 10:
                return int_to_mini_roman(int(number / 10)) + 'x' + int_to_mini_roman(number % 10)
            elif number >= 5:
                return int_to_mini_roman(int(number / 10)) + 'v' + int_to_mini_roman(number % 10)
            else:
                return int_to_mini_roman(int(number / 10)) + int_to_mini_roman(number % 10)
    else:
        return 'Number out of range'

