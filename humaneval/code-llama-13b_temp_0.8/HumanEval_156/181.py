
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
    # numbers dictionary
    numbers = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    # roman numeral string
    roman_numeral = ''
    # check for each number, from the biggest to the smallest
    for n in numbers:
        # get number of times current number can fit in the given number
        times_fit = number // numbers[n]
        # add current number to the roman numeral string that many times
        roman_numeral += n * times_fit
        # substract the value of the current number * number of times it can fit
        # from the number to be converted
        number -= times_fit * numbers[n]
    # return roman numeral
    return roman_numeral

