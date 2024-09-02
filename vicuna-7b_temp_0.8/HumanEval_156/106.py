
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
    roman = ""
    while number > 0:
        digit = number % 10
        if digit > 5:
            number //= 10
            roman += digit - 4 + 5
        else:
            number //= 100
            roman += digit - 3 + 5
        number = number / 100
    return roman.lower()
