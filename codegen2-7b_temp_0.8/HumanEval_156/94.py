
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
    if 1 <= number <= 1000:
        temp = str(number)
        roman_numeral = ''
        for char in temp:
            roman_numeral += _num_to_mini_dict[int(char)]
        return roman_numeral
    else:
        raise ValueError('number must be between 1 and 1000')
