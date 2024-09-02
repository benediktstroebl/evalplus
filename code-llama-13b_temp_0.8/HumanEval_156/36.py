
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

    if number is None or number < 1 or number > 1000:
        raise Exception('Wrong number')

    roman_numeral_map = (
        ('M', 1000), ('CM', 900), ('D', 500),
        ('CD', 400), ('C', 100), ('XC', 90),
        ('L', 50), ('XL', 40), ('X', 10), ('IX', 9),
        ('V', 5), ('IV', 4), ('I', 1)
    )

    result = ''
    for roman_numeral, integer in roman_numeral_map:
        while number >= integer:
            result += roman_numeral
            number -= integer
    return result

