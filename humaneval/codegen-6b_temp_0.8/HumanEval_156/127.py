
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
    if not isinstance(number, int) or number < 1 or number > 1000:
        return ""
    elif number > 1000:
        return ""

    # if number is 1000, return 'c'
    if number == 1000:
        return "c"

    result = ""
    # number < 1000
    while number:
        # find the smallest roman integer that is bigger than number
        if number < 500:
            result += get_roman_numeral(number)
            number = 0
        else:
            # use limit to figure out what to add
            if 500 < number < 1000:
                limit = 999
            elif number < 500:
                limit = 499
            else:
                limit = 999
            # subtract limit from number and add to result
            result += get_roman_numeral(limit)
            number -= limit

    return result.lower()

