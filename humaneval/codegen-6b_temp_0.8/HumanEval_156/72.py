
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
    number_text = ''

    if number < 1:
        raise ValueError('Value out of bounds: {}'.format(number))

    if number < 400:
        for numeral, value in ROW_NUMS.items():
            while number >= value:
                number_text += numeral
                number -= value

    elif number < 500:
        number_text += ROW_NUMS[400]
        number_text += ROW_NUMS[300] * (number - 400)

    elif number < 900:
        number_text += ROW_NUMS[500]
        number_text += ROW_NUMS[400] * (number - 500)

    else:
        number_text += ROW_NUMS[900]
        number_text += ROW_NUMS[500] * (number - 900)

    return number_text.lower()

