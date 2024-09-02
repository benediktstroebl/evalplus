
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
    assert 1 <= number <= 1000, f"number is out of range, {number} > 1000"
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ""
    for i in range(len(value)):
        while number >= value[i]:
            number -= value[i]
            roman += roman_numerals[i]
    return r
