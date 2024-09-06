
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
    # Dictionary of roman numerals as keys and their values as values.
    roman_nums = {1: 'i', 5: 'v', 10: 'x', 50: 'l',
                  100: 'c', 500: 'd', 1000: 'm'}
    res = ""
    # Loop through all the numbers from 1000 to 1 and check if it's a factor.
    for key in sorted(roman_nums.keys(), reverse=True):
        if key <= number:
            # If factor, then obtain quotient and remaind.
            number, remainder = divmod(number, key)
            # Append key to res, remainder of times.
            res += roman_nums[key] * remainder
    return res.lower()

