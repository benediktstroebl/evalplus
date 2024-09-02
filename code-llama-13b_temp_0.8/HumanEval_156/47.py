
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
    mini_roman = ''
    # alphabetically sorted
    roman_numerals = ['i', 'v', 'x', 'l', 'c', 'd', 'm']
    # values of the respective roman numerals
    values = [1, 5, 10, 50, 100, 500, 1000]
    index = 0
    # iterate from the largest roman numeral to the smallest
    while number > 0:
        # find the greatest multiple of the current roman numeral less than number
        multiple = number // values[index]
        # add that multiple of the roman numeral to mini_roman
        mini_roman += roman_numerals[index] * multiple
        # subtract that multiple from number
        number -= values[index] * multiple
        index += 1
    return mini_roman

