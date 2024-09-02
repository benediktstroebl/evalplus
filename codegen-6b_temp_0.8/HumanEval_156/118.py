
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
    assert 1 <= number <= 1000, 'You are out of range.'
    output = ''
    A = 'x'
    D = 'c'
    C = 'c'
    L = 'l'
    X = 'x'
    V = 'v'
    I = 'i'
    if number == 0:
        return ''
    elif number == 1:
        return A
    else:
        while number > 0:
            if number >= 1000:
                output += A
                number -= 1000
            elif number >= 900:
                output += D*(number/900)
                number -= 900
            elif number >= 500:
                output += C
                number -= 500
            elif number >= 400:
                output += L
                number -= 400
            elif number >= 100:
                output += X
                number -= 100
            elif number >= 90:
                output += V
                number -= 90
            elif number >= 50:
                output += I
                number -= 50
            elif number >= 40:
                output += L
                number -= 40
            elif number >= 10:
                output += V
                number -= 10
            elif number >= 9:
                output += I
                number -= 9
            elif number >= 5:
                output += V
                number -= 5
            elif number >= 4:
                output += I
                number -= 4
            elif number >= 1:
                output += V
                number -= 1
    return output.lower()
