
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
    numbers = {1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v',
               6: 'vi', 7: 'vii', 8: 'viii', 9: 'ix', 10: 'x',
               100: 'c', 200: 'cc', 300: 'ccc', 400: 'cd',
               500: 'd', 600: 'dc', 700: 'dcc', 800: 'dccc', 900: 'cm',
               1000: 'm', 2000: 'mm', 3000: 'mmm'}
    roman = []
    for num in reversed(range(1, number + 1)):
        if num not in numbers:
            break
        roman.append(numbers[num])
    return ''.join(roman)

