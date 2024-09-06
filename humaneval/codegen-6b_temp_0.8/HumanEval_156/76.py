
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
    # turn the number into a string of roman numerals
    # (these are numbers 0-10 in roman numerals)
    roman = ''
    while number > 0:
        # find the smallest roman numeral that has this number
        smallest = roman_numerals[number]
        # add the smallest roman numeral to the final roman string
        roman += smallest
        # subtract this roman numeral's number from the number being processed
        number -= roman_numerals[smallest]

    return roman.lower()

