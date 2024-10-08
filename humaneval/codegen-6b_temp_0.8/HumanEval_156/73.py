
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
    d = {1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l',
         90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    mid = ''
    if number in d:
        return d[number]
    else:
        num = int(number)
        if num in d:
            return d[num]
        elif (num % 10) in d:
            mid = d[num % 10]
            return num // 10 * 'm' + d[10] + mid
        elif (num % 100) in d:
            mid = d[num % 100]
            return num // 100 * 'm' + 'l' + mid
        elif (num % 1000) in d:
            mid = d[num % 1000]
            return num // 1000 * 'm' + 'l' + 'v' + mid

