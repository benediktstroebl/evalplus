
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
    # the roman numeral system is the number that is represented by the roman
    # numeral, rather than the letters being the roman numeral
    # so we can use each letter's value to calculate how many times it appears
    # in the roman numeral
    # the letters are already in the correct order, so we can use the letters
    # as the keys and count up the occurrences
    roman_numerals = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000,
    }
    # initialise the return value as a string
    roman = ''
    # find the largest key in the dictionary
    # we can do this by iterating through the roman numerals in reverse order
    for letter in reversed(roman_numerals.keys()):
        # determine how many times the current letter appears in the number
        # this is the number of times the letter's value appears in the number
        # divided by the letter's value
        # for example, 'xix' has 3 'i's, and each 'i' has a value of 1
        # so 3 / 1 = 3
        # 'xii' has 2 'i's, and each 'i' has a value of 1
        # so 2 / 1 = 2
        letter_occurrences = number // roman_numerals[letter]
        # if there are no occurrences, move on to the next letter
        if letter_occurrences == 0:
            continue
        # add the letter to the roman numeral string
        roman += letter * letter_occurrences
        # subract the number of occurrences of the letter from the number
        # this will ensure that the letters do not occur more than once
        # for example, if there are 2 'i's, and 2 'i's have a value of 1
        # then we can subtract 2 * 1 = 2 from 19, giving us 7
        # 7 / 1 = 7
