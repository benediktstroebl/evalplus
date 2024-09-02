
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
    # The following is the full romam_numerals mapping.
    # romam_numerals = {
    #     1000: 'm',
    #     900: 'cm',
    #     500: 'd',
    #     400: 'cd',
    #     100: 'c',
    #     90: 'xc',
    #     50: 'l',
    #     40: 'xl',
    #     10: 'x',
    #     9: 'ix',
    #     5: 'v',
    #     4: 'iv',
    #     1: 'i'
    # }

    romam_numerals = {
        1000: 'm',
        900: 'dcccc',
        500: 'd',
        400: 'cd',
        100: 'c',
        90: 'xc',
        50: 'l',
        40: 'xl',
        10: 'x',
        9: 'ix',
        5: 'v',
        4: 'iv',
        1: 'i'
    }

    # Create a dictionary to map digits to the corresponding romam numerals.
    num_to_romam = {
        '1': 'i',
        '2': 'ii',
        '3': 'iii',
        '4': 'iv',
        '5': 'v',
        '6': 'vi',
        '7': 'vii',
        '8': 'viii',
        '9': 'ix'
    }

    # Convert the given number into a string.
    number = str(number)

    # Iterate through the number and convert each digit to its corresponding
    # romam numeral.
    result = []
    for num in number:
        result.append(num_to_romam[num])
    # Return the romam numeral equivalent as a string, and return it in lowercase.
    return ''.join(result).lower()
