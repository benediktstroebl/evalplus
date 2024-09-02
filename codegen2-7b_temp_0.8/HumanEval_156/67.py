
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
    assert 1 <= number <= 1000
    result = ""
    i = 0
    while number > 0:
        if i == 0 or i == 1:
            result += num_to_char[number]
        else:
            result += num_to_char[number - 2] + num_to_char[i]
        number -= i
        i += 1
    return result.lower
