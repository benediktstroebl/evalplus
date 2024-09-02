
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

    roman = {
        1 : "i",
        5 : "v",
        10 : "x",
        50 : "l",
        100 : "c",
        500 : "d",
        1000 : "m",
        }

    ints = [1000, 500, 100, 50, 10, 5, 1]
    result = []

    for i in ints:
        while number >= i:
            number -= i
            result.append(roman[i])

    return ''.join(result)
