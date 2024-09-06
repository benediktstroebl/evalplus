
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
    if not 1 <= number <= 1000:
        raise ValueError('%s is out of range [1, 1000]' % number)

    # Since we are dealing with integers, we can divide by 1000
    # each time to obtain the number of 1000's (or more) to include
    # in our roman numeral.
    roman_numerals = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }

    result = []
    for value, numeral in roman_numerals.items():
        count = number // value
        # In the case that the remainder is a multiple of 5,
        # we need to include both the numeral for 5 and 10
        # (or 50 and 100, etc)
        if number % value == 0 and number % (value * 5) == 0:
            result.append(numeral * (number // (value * 5)))
            number %= value * 5
        # In the case that the remainder is a multiple of 10,
        # we need to include the numeral for 10
        elif number % value == 0 and number % (value * 10) == 0:
            result.append(numeral * (number // (value * 10)))
            number %= value * 10
        # Otherwise, we can just simply append the numeral for
        # each value, and decrement the remainder to continue
        # the loop
        else:
            result.append(numeral * count)
            number -= value * count

    return ''.join(result).lower()

