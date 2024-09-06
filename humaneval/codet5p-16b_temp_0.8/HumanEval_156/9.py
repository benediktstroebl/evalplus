
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

    assert number <= 1000 and number >= 1, "Invalid input"

    roman = ""
    value = 1
    
    while number > 0:
        if value <= number:
            roman += int_to_mini_roman_helper(value)
            number -= value
        else:
            value *= 10
    return roman.lower()
