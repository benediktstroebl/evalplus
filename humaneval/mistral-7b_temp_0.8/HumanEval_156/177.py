
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

    for i in range(1, 10):
        roman.append('i' * i)

    for i in range(10, 100):
        roman.append('v' + roman[i // 10] + 'i' * (i % 10))

    for i in range(100, 1000):
        roman.append('c' + roman[i // 100] + 'h' * (i % 100 // 10) +
                     'x' * (i % 10))

    roman.append('m' + 'c' * 9 + 'x' + 'i' + 'v' + 'i')

    roman.append('mm' + 'c' * 9)

    roman.append('x' + 'c' * 9)

    roman.append('c' + 'c' * 9)

    roman.append('cc' + 'c' * 8)

    roman.append('d' + 'c' *
