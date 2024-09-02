
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
    mini_roman = ""
    largest_val = 9
    largest_numeral = 'ix'
    for i in range(17):
        val = (number / largest_val) * largest_numeral
        number = number % largest_val
        if val >= 10:
            if val >= 10:
                val = 'x'
            else:
                val = 'i'
        mini_roman += val
        if len(mini_roman) > 4:
            return 'Error'
    return mini_roman

