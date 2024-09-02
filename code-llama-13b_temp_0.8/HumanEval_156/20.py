
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
    # Because the integer we are converting is always within the range [1, 1000],
    # the string that we will use to return the roman numeral is already created.
    mini_roman_dict = {'1': 'i', '5': 'v', '10': 'x', '50': 'l', '100': 'c',
                       '500': 'd', '1000': 'm', '4': 'iv', '9': 'ix', '40': 'xl',
                       '90': 'xc', '400': 'cd', '900': 'cm'}
    mini_roman = ''
    if 0 < number <= 1000:
        if number == 1000:
            mini_roman = 'm'
        else:
            # Turn the number into a string so that we can loop over it.
            number_as_str = str(number)
            for digit in number_as_str:
                mini_roman += mini_roman_dict[digit]
    else:
        raise ValueError('Invalid input: {} is not within the required range.'
                         .format(number))
    return mini_roman
