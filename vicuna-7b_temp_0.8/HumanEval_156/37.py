
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
        digit = number % 1000
        if digit < 10:
            digit = 0
        number //= 1000
        if digit == 4 or digit == 6 or digit == 9:
            digit = "I"
        elif digit == 5:
            digit = "V"
        else:
            digit = "X"
        roman += digit
    return roman[::-1]
