
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
    if not isinstance(number, int) or number <= 0:
        raise ValueError(
            'You must provide a positive integer greater than 0. Got: {}'.format(number))

    if number > 1000:
        raise ValueError('The input number must be lesser or equal to 1000')

    # Dict containing the Roman numerals as keys and their values
    roman = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }

    # The result is a string
    result = ''

    # Get the list of keys ordered by value
    keys = sorted(roman, reverse=True)

    # Loop over the keys to build the Roman numeral
    for key in keys:
        # Get the number of times that the current key fits in the number
        count = number // key
        # If there is no count, continue to the next key
        if count == 0:
            continue

        # Build the Roman numeral using the current key
        result += roman[key] * count

        # Subtract the number of times that the key fits in the number from the number
        number -= count * key

    return result

