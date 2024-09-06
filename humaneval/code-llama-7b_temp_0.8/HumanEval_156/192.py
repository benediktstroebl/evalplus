
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
    res = ""
    if number / 1000:
        res = res + "m" * (number / 1000)
        number = number % 1000
    if number / 500:
        res = res + "d"
        number = number % 500
    if number / 100:
        res = res + "c" * (number / 100)
        number = number % 100
    if number / 50:
        res = res + "l"
        number = number % 50
    if number / 10:
        res = res + "x" * (number / 10)
        number = number % 10
    if number / 5:
        res = res + "v"
        number = number % 5
    if number:
        res = res + "i" * (number)
    return res.lower()
