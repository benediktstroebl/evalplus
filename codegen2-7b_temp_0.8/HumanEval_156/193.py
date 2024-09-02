
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
    if number < 1 or number > 1000:
        raise ValueError("only number between 1 and 1000")
    return_list = []
    for i in range(0,number):
        return_list.append(numeral_to_roman(i))
    return ''.join(return_list).lower()
