
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
    roman_numerals = [None] * 10

    # Helper function to convert the number to a string
    def to_str(i):
        if i < 10:
            return f'{i}'
        i -= 10
        roman_numerals[i] = f'{i}'
        while i > 0:
            roman_numerals[i] += f'{i % 10}'
            i = i / 10
    to_str(number)

    # Generate the list of roman numerals for the number
    for i in range(10):
        roman_numerals[i] = roman_numerals[i][:-2]
    if number > 1000:
        roman_numerals[-1] = 'M' + roman_numerals[-1]
    if number >= 1000:
        roman_numerals[-1] += str(number - 1000)

    return ' '.join(roman_numerals)