
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

    # determine the hundreds, tens, and ones
    hundreds = number // 100
    tens = number % 100 // 10
    ones = number % 10

    # initialize the return string
    roman_numeral = ""

    # add the hundreds, if it exists
    if hundreds > 0:
        roman_numeral = roman_numeral + hundreds_map[hundreds]

    # add the tens, if it exists
    if tens > 0:
        roman_numeral = roman_numeral + tens_map[tens]

    # add the ones, if they exist
    if ones > 0:
        roman_numeral = roman_numeral + ones_map[ones]

    # return the answer
    return roman_numeral.lower()

