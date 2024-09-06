
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
    num_to_roman = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }

    roman = ''
    for i in range(1, 1000):
        # num_to_roman[i] is None if i does not have a roman equivalent
        if num_to_roman[i] is not None:
            # get the number of times i is in number
            num = number // i
            number = number % i
            roman += num_to_roman[i] * num

    return roman
