
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
    # only integers greater or equal to 1
    # and less or equal to 1000 are accepted
    if type(number) is not int or number < 1 or number > 1000:
        return

    roman_values = [
        1000,
        900, 500,
        400, 100,
        90, 50,
        40, 10,
        9, 5,
        4, 1
    ]
    roman_letters = [
        'm',
        'cm', 'd',
        'cd', 'c',
        'xc', 'l',
        'xl', 'x',
        'ix', 'v',
        'iv', 'i'
    ]

    # create the empty result string
    result = ''
    # for every value in roman values
    for i in range(len(roman_values)):
        # check if the number is greater or equal
        # than the actual roman value
        while number >= roman_values[i]:
            # append the roman letter equivalent to the result string
            result += roman_letters[i]
            # subtract the roman value from the number
            number -= roman_values[i]

    return result.lower()

