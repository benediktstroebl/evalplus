
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
        raise TypeError('Expected integer, but got %s' % number.__class__.__name__)
    if number <= 0:
        raise ValueError('Only positive integers are allowed')
    if number > 1000:
        raise ValueError('Number must be <= 1000')
    roman_numerals = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000,
    }
    # The digit value for each digit.
    # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1.
    digits = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_numbers = []
    for digit in digits:
        count = number // digit
        roman_numbers.append(roman_numerals[digit / 100] * (digit / 100))
        roman_numbers.append(roman_numerals[digit / 10] * (digit / 10 % 10))
        roman_numbers.append(roman_numerals[digit % 10] * count)
        number -= digit * count
    return ''.join(roman_numbers).lower()

