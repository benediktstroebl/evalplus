
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
    if number >= 4000 or number < 1:
        return None

    roman = ''
    for i in reversed(range(len(int_to_roman(number)))):
        if int_to_roman(number)[i] == 'I':
            roman += int_to_roman(number)[i]
            number = number - 10**i
        else:
            roman += int_to_roman(number)[i]

    return roman
