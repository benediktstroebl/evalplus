
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

    if number > 1000 or number < 1:
        raise ValueError('The number should be between 1 and 1000')
    dictionary = {1: 'x', 4: 'x', 5: 'ix', 9: 'x', 10: 'x', 40: 'xx', 50: 'x', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000:'m'}
    ans = ''
    while number!= 0:
        if number < 4:
            ans += dictionary[1]
            number -= 1
        elif number >= 4 and number < 9:
            ans += dictionary[4]
            number -= 4
        elif number == 9:
            ans += dictionary[5]
            number -= 9
        elif number >= 10 and number < 40:
            ans += dictionary[10]
            number -= 10
        elif number == 40:
            ans += dictionary[40]
            number -= 40
        elif number >= 50 and number < 90:
            ans += dictionary[50]
            number -= 50
        elif number == 90:
            
