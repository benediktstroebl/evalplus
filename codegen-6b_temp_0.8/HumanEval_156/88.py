
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
    assert 1 <= number <= 1000, 'Number must be between 1 and 1000'
    assert isinstance(number, int), 'Number must be int'
    roman = ''
    digits = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    for i in range(len(digits)):
        while number >= digits[i]:
            number -= digits[i]
            roman += symbols[i]
    return roman.lower()
