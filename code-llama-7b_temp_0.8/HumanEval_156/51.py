
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
    # base case: if number is 0, return empty string
    if number <= 0:
        return ''
    # keep track of our return value
    ret_val = ''
    # while number is greater than 0
    while number > 0:
        # check if number is divisible by 10
        if number >= 10:
            # if so, divide by 10
            number /= 10
            # and append 'x' to ret_val
            ret_val += 'x'
        # check if number is divisible by 5
        elif number >= 5:
            # if so, divide by 5
            number /= 5
            # and append 'v' to ret_val
            ret_val += 'v'
        # check if number is divisible by 4
        elif number >= 4:
            # if so, divide by 4
            number /= 4
            # and append 'iv' to ret_val
            ret_val += 'iv'
        # check if number is divisible by 1
        elif number >= 1:
            # if so, divide by 1
            number /= 1
            # and append 'i' to ret_val
            ret_val += 'i'
    # return ret_val (lowercase)
    return ret_val.lower()
