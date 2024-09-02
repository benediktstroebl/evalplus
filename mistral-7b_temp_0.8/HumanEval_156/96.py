
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
    # handle base cases
    if number <= 0 or number > 1000:
        raise Exception

    roman_num = ''

    # iterate over 1000s, 100s, 10s, and 1s
    # and append corresponding symbols to roman_num
    # and subtract 1000, 100, 10, or 1 from num as you go
    while number > 0:
        if number >= 1000:
            roman_num += 'm'
            number -= 1000
        elif number >= 100:
            roman_num += 'c'
            number -= 100
        elif number >= 10:
            roman_num += 'x'
            number -= 10
        else:
            roman_num += 'i'
            number -= 1

    return roman_num

