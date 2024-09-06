
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
    if not 0 <= number <= 1000:
        raise ValueError('number must be between 1 and 1000')
    roman_nums = [None, '','m','mm','mmm','mmmm','mmmmm']
    return roman_nums[number - 1]

