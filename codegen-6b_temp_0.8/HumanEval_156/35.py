
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
    roman_mapping = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }

    # Check if the number is out of range
    if not (1 <= number <= 1000):
        raise ValueError('The number should be between 1 and 1000 inclusive')

    # Utilize a list comprehension to get each value in the range
    # in the roman numeral mapping
    return ''.join(roman_mapping[num] for num in [
        num for num in range(1, number + 1)
        if num in roman_mapping
    ])

