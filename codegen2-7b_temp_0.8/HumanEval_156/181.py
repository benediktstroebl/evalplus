
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
    if not isinstance(number, int):
        raise TypeError("Input must be a positive integer")
    if number < 1 or number > 1000:
        raise ValueError("Input must be a positive integer between 1 and 1000")

    roman = ''

    while number > 0:
        num = number % 10
        if num == 1:
            roman = 'i' + roman
        elif num == 2:
            roman = 'ii' + roman
        number = number // 10
    
