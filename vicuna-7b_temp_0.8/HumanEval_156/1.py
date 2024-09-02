
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
    roman = []
    digit = 0
    while number != 0:
        if number % 1000 == 1000:
            roman.append('M')
        if number % 1000 == 500:
            roman.append('D')
        if number % 1000 == 100:
            roman.append('C')
        if number % 1000 == 50:
            roman.append('L')
        if number % 1000 == 10:
            roman.append('X')
        if number % 1000 == 5:
            roman.append('XL')
        if number % 1000 == 1:
            roman.append('XC')
        if number % 1000 == 5:
            roman.append('XL')
        if number % 1000 == 100:
            roman.append('C')
        if number % 1000 == 500:
            roman.append('D')
        if number % 1000 == 100:
            roman.append('M')
        number //= 1000
        digit += 1
    roman.append('I')
    return ' '.join(roman)[:-2] + 'a'