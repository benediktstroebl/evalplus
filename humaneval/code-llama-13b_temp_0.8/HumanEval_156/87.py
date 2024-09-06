
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
    # dictionary containing the conversion from arabic to roman numerals
    conversions = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
        'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }
    # to store the roman numeral
    roman = ''
    # iterate over the dictionary's keys and values
    for key in conversions.keys():
        # check if the number is still greater than the current conversion value
        while number >= conversions[key]:
            # if so, append the key to the roman numeral
            roman += key
            # and subtract the conversion value from the number
            number -= conversions[key]
    # return the lowercase version of the roman numeral
    return roman.lower()

