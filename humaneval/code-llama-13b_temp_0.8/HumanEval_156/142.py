
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
    # create dictionary to store the roman numerals
    d = {1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 90: 'xc', 50: 'l',
         40: 'xl', 10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'}
    # initiate the output string
    output = ''
    # for each of the dictionary keys, add the roman numeral equivalent to the
    # output string
    for num in d:
        # divide the number by the current dictionary key
        div = number / num
        # while the number is greater or equal to the current dictionary key
        while div >= 1:
            # add the roman numeral equivalent of the current dictionary key
            # to the output string
            output += d[num]
            # subtract the current dictionary key from the number
            number -= num
            # divide the number by the current dictionary key
            div = number / num
    return output

