
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
    # 1. build a dictionary of roman values
    roman_values = {
        1000: 'm',
        900: 'cm',
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
        1: 'i',
    }
    # 2. build a list of keys from dictionary in reverse order
    keys = sorted(roman_values.keys(), reverse=True)
    # 3. initialize result as empty string
    result = ''
    # 4. loop through dictionary using keys
    for key in keys:
        # 5. obtain quotient of number / key
        num_key = number // key
        # 6. if num_key is greater than 0, update result
        if num_key > 0:
            result += roman_values[key] * num_key
        # 7. redefine number
        number -= key * num_key
    return result.lower()

