
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
    number = int(number)
    if number == 0:
        return ''
    elif number < 0 or number > 1000:
        raise ValueError("Expected value to be in the range [1, 1000]")
    result = ''
    while number != 0:
        if number >= 900:
            result += 'cm'
            number -= 900
        elif number >= 500:
            result += 'd'
            number -= 500
        elif number >= 400:
            result += 'cd'
            number -= 400
        elif number >= 100:
            if number >= 90:
                result += 'xc'
                number -= 90
            elif number >= 50:
                result += 'l'
                number -= 50
            elif number >= 40:
                result += 'xl'
                number -= 40
            elif number >= 10:
                if number >= 9:
                    result += 'ix'
                    number -= 9
                elif number >= 5:
                    result += 'v'
                    number -= 5
                elif number >= 4:
                    result += 'iv'
                    number -= 4
                else:
                    result += 'i'
                    number -= 1
        else:
            if number >= 90:
                result += 'xci'
                number -= 90
            elif number >= 50:
                result += 'li'
                number -= 50
            elif number >= 40:
                result += 'lx'
                number -= 40
            elif number >= 10:
                if number >= 9:
                    result += 'ix'
                    number -= 9
                elif number >= 5:
                    result += 'v'
                    number -= 5
                elif number >= 4:
                    result += 'iv'
                    number -= 4
                else:
                    result += 'i'
                    number -= 1
    return result

