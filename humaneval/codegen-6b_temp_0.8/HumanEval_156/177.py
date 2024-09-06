
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
    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError("int_to_mini_roman expected a positive number between 1 and 1000")

    roman_numerals = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
    numbers = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    numeral = ''
    for i, n in enumerate(numbers):
        count = number // n
        number %= n
        if count > 0:
            numeral += roman_numerals[i] * count
    return numeral.lower()

