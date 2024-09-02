
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

    d = {1 : "i", 5 : "v", 10 : "x"}

    roman = []

    for key in d.keys():
        x = number // key
        roman.append(x * d[key])
        number = number % key

    return "".join(roman).lower()

