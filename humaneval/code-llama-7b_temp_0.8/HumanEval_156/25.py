
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
    value_map = {
        1000: "m", 
        900: "cm", 
        500: "d", 
        400: "cd", 
        100: "c", 
        90: "xc", 
        50: "l", 
        40: "xl", 
        10: "x", 
        9: "ix", 
        5: "v", 
        4: "iv", 
        1: "i"
    }
    # consider if number is less than 1 or greater than 1000
    if number < 1 or number > 1000:
        return "number must be between 1 and 1000"
    else:
        # return the number in roman numerals as a string
        return ''.join([value_map[value] for value in value_map if value <= number])
