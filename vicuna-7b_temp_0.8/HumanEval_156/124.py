
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
    roman = []
    while number > 0:
        # add the last digit to the end of the string
        roman.append(str(number % 10))
        number //= 10
        # if the number is greater than 100, it's the last digit
        # of a single digit number, so we don't need to convert it
        if number == 0:
            break
    return ''.join(roman)
