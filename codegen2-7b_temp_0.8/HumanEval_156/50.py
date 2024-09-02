
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
    
    return_string = ''
    
    while number > 0:
        if number < 1000:
            return_string += str(number)
            break
        elif number == 1000:
            return_string +='m'
            break
        else:
            if number < 4000:
                return_string +='m' + str(number)
            else:
                return_string += 'cd' + int_to_mini_roman(number % 1000)
        number /= 1000
    return return_
