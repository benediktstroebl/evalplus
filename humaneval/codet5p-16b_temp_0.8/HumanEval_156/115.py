
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

    numbers_dict = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }

    num_roman = ''

    for i in numbers_dict:
        if number > 1000:
            print('The number is out of the range of the given restrictions')
            return None

        if number >= i:
            num_roman += numbers_dict[i] * (number // i)
            number %= i

    return num_roman.lower()
