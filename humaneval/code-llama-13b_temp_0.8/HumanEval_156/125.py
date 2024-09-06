
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
    integer_map = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }
    roman_numerals = []

    # Split the number into digits
    digits = []
    while number:
        digits.append(number % 10)
        number //= 10

    # Get the equivalent roman numeral for each digit
    for digit in digits:
        if digit == 0:
            continue
        elif digit == 4:
            roman_numerals.append(integer_map[5] + integer_map[1])
        elif digit == 9:
            roman_numerals.append(integer_map[1] + integer_map[10])
        else:
            roman_numerals.append(integer_map[digit])

    return ''.join(reversed(roman_numerals))

