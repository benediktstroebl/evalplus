
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
    # Test for edge cases
    if number >= 4000 or number < 0:
        raise ValueError

    # Convert the number into an integer
    i = int(number)

    # Initialize empty list to store the roman numeral equivalent
    roman_numeral = []

    # Iteratively update list with roman numeral equivalent
    while i >= 1000:
        roman_numeral.append('M')
        i = i - 1000

    while i >= 500:
        roman_numeral.append('D')
        i = i - 500

    while i >= 100:
        roman_numeral.append('C')
        i = i - 100

    while i >= 50:
        roman_numeral.append('L')
        i = i - 50

    while i >= 10:
        roman_numeral.append('X')
        i = i - 10

    while i >= 5:
        roman_numeral.append('V')
        i = i - 5

    while i >= 1:
        roman_numeral.append('I')
        i = i - 1

    # Return list as string
    return ''.join(roman_numeral)

