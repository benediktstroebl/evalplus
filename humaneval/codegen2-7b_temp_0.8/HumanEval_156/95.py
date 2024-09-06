
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
    if number <= 0:
        raise ValueError("number should be positive.")
    elif number > 1000:
        raise ValueError("number should not be larger than 1000.")
    else:
        result = []
        for i in range(1, number+1):
            result.append(int_to_roman(i))
        return ''.join(result).lower
