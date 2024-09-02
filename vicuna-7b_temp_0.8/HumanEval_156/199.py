
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
    sign = 'I'
    if number > 0:
        for i in range(4):
            digits = str(number % 100)
            roman += digits
            number /= 100
            if number > 0:
                sign = 'V'
                if number > 0:
                    sign = 'X'
                    number %= 1000
                else:
                    sign = 'I'
                    number = 0
                    i -= 1
    return sign + roman[::-1]
