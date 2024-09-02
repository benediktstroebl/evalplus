
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
    numeral = ''
    for i in range(len(str(number))):
        numeral += str(number // 1000)
        number = number % 1000
        if number == 0:
            break
    numeral += str(number // 100)
    number = number % 100
    if number == 0:
        numeral += 'CM'
    else:
        numeral += 'XC'
    return numeral.lower()
