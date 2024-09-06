
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
    i = 0

    while number >= 1000:
        roman += str(number / 1000).zfill(2)
        number = number % 1000
        i += 1

    if number > 0:
        roman += str(number).zfill(2)

    return roman[::-1].lower()
